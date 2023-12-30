import os,json,requests
from flask import Flask, render_template, request, jsonify
from DbHandler.dbFile import dbSearch,dbHashSearch,fileScanResult,dbURLSearch,SearchIPCount,SearchURLCount,countdbhashValues,countdbIPAddresses,countdbUrls,UploadFileCount
from flask_socketio import SocketIO
import initialSetup
from fileScripts.hashgenerator import hash_file
from fileScripts.vthashscan import VT_Request
from ipScripts.vt import checkIP
from ipScripts.vt import checkURL
from threatnews import latestIoC
from ipScripts.kasperskyip import kasperskyIP
from fileScripts.kshashscan import kasperskyHash
from ipScripts.kasperskyurl import kasperskyURL
from ipScripts.honeydb import honeyDB
from ipScripts.abuseIPDB import abuseIPDBFunc

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
    searchIPCount = SearchIPCount(0)
    searchURLCount = SearchURLCount(0)
    uploadedfileCount = UploadFileCount(0)

    countDbUrls = countdbUrls()
    countdbIpAddresses = countdbIPAddresses()
    countdbHashhValues = countdbhashValues()
    # return render_template('home.html', result=result)
    return render_template('home.html', result=result,searchIPCount=searchIPCount,searchURLCount=searchURLCount,uploadedfileCount=uploadedfileCount,\
                            countdbhashValues=countdbHashhValues,countdbIPAddresses=countdbIpAddresses,\
                            countdbUrls=countDbUrls)

@app.route("/about")
def aboutPage():
    return render_template('about.html')

@app.route("/services")
def servicesPage():
    return render_template('services.html')

@app.route("/contact")
def contactPage():
    return render_template('contact.html')

@app.route('/checkentity',methods=["GET"])
def checkentitiy():
    result = None
    if request.method == 'GET':

        # ip = request.form.get('q')
        ip = request.args.get('ip')
        if len(ip)<=10:
        # print(ip)
            result = dbSearch(ip)
            # print(result)
            checkCount = SearchIPCount(1)
        
            socket.emit("checkentity",{'dbResult':result,'checkCount':checkCount,'countType':'ip'})      
            return jsonify(isError = False,
                            message = "Success",
                            statusCode = 200,
                            data = result), 200
        else:
            socket.emit("errormsg",{'errorMsg':"Length exceeded."})      
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
            if len(ip) <=10:
    
                result = checkIP(ip)
                socket.emit("checkvtip",{'vtResult':(result)})      
                return jsonify(isError = False,
                                message = "Success",
                                statusCode = 200,
                                data = result), 200
            else:
                socket.emit("errormsg",{'errorMsg':"Length exceeded."})      
                return jsonify(isError = False,
                            message = "Success",
                            statusCode = 200,
                            data = result), 200 
            # print("VT IP: ",ip)
        except Exception as e:
            print(e)
        # result = checkIP(ip)
        # print(result)        
        # print(type(result))

    

@app.route('/checkurl',methods=["GET"])
def checkurl():
    result = None
    if request.method == 'GET':

        # ip = request.form.get('q')
        url = request.args.get('url')
        if len(url) <=50:
        # print(ip)
            result = dbURLSearch(url)
            checkCount = SearchURLCount(1)

        # print(result)

            socket.emit("checkentity",{'dbResult':result,"checkCount":checkCount,'countType':'url'})      
            return jsonify(isError = False,
                            message = "Success",
                            statusCode = 200,
                            data = result), 200
        else:
            socket.emit("errormsg",{'errorMsg':"Length exceeded."})      
            return jsonify(isError = False,
                        message = "Success",
                        statusCode = 200,
                        data = result), 200 


@app.route('/checkvturl',methods=["GET"])
def checkvturl():
    result = None
    if request.method == 'GET':
        try:
            url = request.args.get('url')
            if len(url) <=50:
                result = checkURL(url)
                socket.emit("checkvtip",{'vtResult':(result)})      
                return jsonify(isError = False,
                                message = "Success",
                                statusCode = 200,
                                data = result), 200
            else:
                socket.emit("errormsg",{'errorMsg':"Length exceeded."})      
                return jsonify(isError = False,
                            message = "Success",
                            statusCode = 200,
                            data = result), 200 
        except Exception as e:
            print(e)
        # print(type(result))

    

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
    requests.get(f"http://127.0.0.1:5000/checkkshash?hashValue={fileHashValue}")
    result = dbHashSearch(fileHashValue)
    checkCount = UploadFileCount(1)
    fileScanResult(fileHashValue,{"db":result})
    
    socket.emit("checkHashValue",{'dbResult':result, 'checkCount':checkCount,'countType':'fileName'})      
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
        if len(url)<=50:
            result = checkURL(url)
            socket.emit("checkurlentity", {'urlResult': result})
            return jsonify(isError=False, message="Success", statusCode=200, data=result), 200
        else:
            socket.emit("errormsg",{'errorMsg':"Length exceeded."})      
            return jsonify(isError = False,
                        message = "Success",
                        statusCode = 200,
                        data = result), 200 

@app.route('/checkvthash',methods=["GET"])
def checkvthash():
    result = None
    if request.method == 'GET':
        try:
            hashValue = request.args.get('hashValue')
        except Exception as e:
            print(e)
        result = VT_Request(hashValue)
        fileScanResult(hashValue,{"vt":result["Status"]})
        # print(type(result))

    socket.emit("checkvthash",{'vtResult':(result)})      
    return jsonify(isError = False,
                    message = "Success",
                    statusCode = 200,
                    data = result), 200

@app.route('/checkksip', methods=["GET"])
def checkksip():
    result = None
    if request.method == 'GET':
        ipValue = request.args.get('ip')
        if len(ipValue)<=10:
            result = kasperskyIP(ipValue)
            socket.emit("checkksipresult", {'ipResult': result})
            return jsonify(isError=False, message="Success", statusCode=200, data=result), 200
        else:
            socket.emit("errormsg",{'errorMsg':"Length exceeded."})      
            return jsonify(isError = False,
                        message = "Success",
                        statusCode = 200,
                        data = result), 200 

    
@app.route('/honeyDBIP', methods=["GET"])
def checkhoneydbip():
    result = None
    if request.method == 'GET':
        ipValue = request.args.get('ip')
        if len(ipValue)<=10:
            result = honeyDB(ipValue)
            # print("Result from HoneyDB: ",result)
            socket.emit("checkhoneydbipresult", {'ipResult': result})
        else:
            socket.emit("errormsg",{'errorMsg':"Length exceeded."})      

    return jsonify(isError=False, message="Success", statusCode=200, data=result), 200

@app.route('/abuseDBIP', methods=["GET"])
def abuseDBIP():
    result = None
    if request.method == 'GET':
        ipValue = request.args.get('ip')
        if len(ipValue)<=10:
            result = abuseIPDBFunc(ipValue)
        # print("Result from abuse ip db: ",result)
            socket.emit("checkabusedbipresult", {'ipResult': result})
        else:
            socket.emit("errormsg",{'errorMsg':"Length exceeded."})      
    return jsonify(isError=False, message="Success", statusCode=200, data=result), 200


@app.route('/checkkshash',methods=["GET"])
def checkkshash():
    result = None
    if request.method == 'GET':
        try:
            hashValue = request.args.get('hashValue')
        except Exception as e:
            print(e)
        result = kasperskyHash(hashValue)
        fileScanResult(hashValue,{"ks":result['Status']})
        # print(type(result))

    socket.emit("checkksipresult",{'ipResult':result})      
    return jsonify(isError = False,
                    message = "Success",
                    statusCode = 200,
                    data = result), 200

@app.route('/checkksurl',methods=["GET"])
def checkksurl():
    result = None
    if request.method == 'GET':
        try:
            url = request.args.get('url')
            if len(url)<=50:
                result = kasperskyURL(url)
                socket.emit("checkksipresult",{'ipResult':result})      
            else:
                socket.emit("errormsg",{'errorMsg':"Length exceeded."})      

        except Exception as e:
            print(e)
        # print(type(result))

    return jsonify(isError = False,
                    message = "Success",
                    statusCode = 200,
                    data = result), 200

if __name__ == "__main__":
    socket.run(app,debug=True)
    # app.run(debug=True)
