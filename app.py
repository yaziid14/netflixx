from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

MONGODB_CONNECTION_STRING = "mongodb+srv://azharyazied2:14juni2002@cluster0.4uh4rdq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGODB_CONNECTION_STRING)
db = client.netflixx


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/akun', methods=["POST"])
def akun():
    email_receive = request.form.get('email_give')
    password_receive = request.form.get('password_give')

    today = datetime.now()
    mytime1 = today.strftime('%Y-%m-%d')
    mytime2 = today.strftime('%H-%M-%S')

    doc = {
        'email': email_receive,
        'password': password_receive,
        'tanggal': mytime1,
        'jam': mytime2
    }
    db.login.insert_one(doc)
    return jsonify({'result': 'success'})


@app.route('/akunn')
def akunn():
    return render_template('akun.html')


@app.route('/tampil')
def tampil():
    tampil_list = list(db.login.find({}, {'_id': False}))
    return jsonify({
        'daftarakun': tampil_list,
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
