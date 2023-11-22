import os,json,requests
from flask import Flask, render_template, request, jsonify
from DbHandler.dbFile import dbSearch,dbHashSearch
from flask_socketio import SocketIO
import initialSetup
from fileScripts.hashgenerator import hash_file
from fileScripts.vthashscan import VT_Request
from ipScripts.vt import checkIP
from ipScripts.vt import checkURL
from threatnews import latestIoC


UPLOAD_FOLDER = 'Uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','zip','exe'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = "BROWNRING"
socket = SocketIO(app)




@app.route('/', methods=['GET', 'POST'])
# def threat_intel():
def index():
    result = latestIoC()
    return render_template('home.html', result=result)

@app.route("/about")
def aboutPage():
    return render_template('about.html')

@app.route("/services")
def servicesPage():
    return render_template('services.html')




@app.route('/checkentity',methods=["GET"])
def checkentitiy():
    result = None
    if request.method == 'GET':

        # ip = request.form.get('q')
        ip = request.args.get('ip')
        # print(ip)
        result = dbSearch(ip)
        # print(result)

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
        result = checkIP(ip)
        # print(result)        
        # print(type(result))

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
    fileHashValue = hash_file(filePath)
    print("Hash: ",fileHashValue)

    requests.get(f"http://127.0.0.1:5000/checkvthash?hashValue={fileHashValue}")
    result = dbHashSearch(fileHashValue)


    socket.emit("checkHashValue",{'dbResult':result})      
    return jsonify(isError = False,
                    message = "Success",
                    statusCode = 200,
                    data = result), 200



#  for url 

@app.route('/checkurlentity', methods=["GET"])
def checkurlentity():
    result = None
    if request.method == 'GET':
        url = request.args.get('url')
        result = checkURL(url)

    socket.emit("checkurlentity", {'urlResult': result})
    return jsonify(isError=False, message="Success", statusCode=200, data=result), 200




@app.route('/checkvthash',methods=["GET"])
def checkvthash():
    result = None
    if request.method == 'GET':
        try:
            hashValue = request.args.get('hashValue')
            print("VT hashValue: ",hashValue)
        except Exception as e:
            print(e)
        result = VT_Request(hashValue)
        print(result)        
        # print(type(result))

    socket.emit("checkvthash",{'vtResult':(result)})      
    return jsonify(isError = False,
                    message = "Success",
                    statusCode = 200,
                    data = result), 200

if __name__ == "__main__":
    socket.run(app,debug=True)
    # app.run(debug=True)
