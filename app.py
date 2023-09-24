from flask import Flask, render_template, request
from ipScripts.dbFile import dbSearch

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def threat_intel():
    result = None
    if request.method == 'POST':
        ip = request.form.get('q')
        print(ip)
        result = dbSearch(ip)
    return render_template('home.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
