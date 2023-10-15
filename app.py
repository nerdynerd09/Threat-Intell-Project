import os
from flask import Flask, render_template, request, jsonify
from ipScripts.dbFile import dbSearch
from flask_socketio import SocketIO
import initialSetup
from fileScripts.hashgenerator import hash_file

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

@app.route('/checkentity',methods=["GET","POST"])
def checkentitiy():
    result = None
    if request.method == 'POST':
        ip = request.form.get('q')
        print(ip)
        result = dbSearch(ip)
        print(result)

    socket.emit("checkentity",{'dbResult':result})      
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
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], fileName))
    return '''
    File uploaded successfuly
    '''
@app.route("/checkFile",methods=["GET"])
def fileCheck():
    if request.method == "GET":
        fileName = request.args.get('fileName')
        print("FileName: ",fileName)

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
