import os,json
from flask import Flask, render_template, request, jsonify
from ipScripts.dbFile import dbSearch
from flask_socketio import SocketIO
import initialSetup
from fileScripts.hashgenerator import hash_file
from ipScripts.vt import checkIP

UPLOAD_FOLDER = 'Uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','zip','exe'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = "BROWNRING"
socket = SocketIO(app)




@app.route('/', methods=['GET', 'POST'])
# def threat_intel():
def index():
    result = None
    # if request.method == 'POST':
    #     ip = request.form.get('q')
    #     print(ip)
    #     result = dbSearch(ip)
    return render_template('home.html', result=result)
    # return render_template('home.html')

@app.route('/checkentity',methods=["GET"])
def checkentitiy():
    result = None
    if request.method == 'GET':

        # ip = request.form.get('q')
        ip = request.args.get('ip')
        print(ip)
        result = dbSearch(ip)
        print(result)

    socket.emit("checkentity",{'dbResult':result})      
    return jsonify(isError = False,
                    message = "Success",
                    statusCode = 200,
                    data = result), 200

@app.route('/checkvtip',methods=["GET"])
def checkvtip():
    result = None
    if request.method == 'GET':
        try:
            ip = request.args.get('ip')
            print("VT IP: ",ip)
        except Exception as e:
            print(e)
        result = (checkIP(ip))
        print(result)        
        print(type(result))

    socket.emit("checkvtip",{'vtResult':(result)})      
    return jsonify(isError = False,
                    message = "Success",
                    statusCode = 200,
                    data = result), 200

    # return render_template('home.html',result=result)

@app.route('/fileUpload',methods=["GET","POST"])
def fileUpload():
    if request.method == 'POST':   
        f = request.files['file'] 
        fileName = f.filename
        try:
            if "Uploads" in os.getcwd():
                f.save(os.path.join(os.getcwd(),fileName))
            else:
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], fileName))
        except Exception as e:
            print("file upload exception: ",e)

    return '''
    File uploaded successfuly
    '''
@app.route("/checkFile",methods=["GET"])
def fileCheck():
    if request.method == "GET":
        fileName = request.args.get('fileName')
        print("FileName: ",fileName)

    if "Uploads" in os.getcwd():
        filePath = os.path.join(os.getcwd(),fileName)
    else:
        os.chdir("Uploads")
        filePath = os.path.join(os.getcwd(),fileName)
    print(filePath)
    print("Hash: ",hash_file(filePath))

    return '''
    File uploaded successfuly
    '''

if __name__ == "__main__":
    socket.run(app,debug=True)
    # app.run(debug=True)
