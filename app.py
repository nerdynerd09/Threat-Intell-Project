from flask import Flask, render_template, request, jsonify
from ipScripts.dbFile import dbSearch
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "BROWNRING"
socket = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def threat_intel():
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


if __name__ == "__main__":
    socket.run(app,debug=True)
    # app.run(debug=True)
