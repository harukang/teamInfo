from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://teami:itogether@cluster0.2tv5dd1.mongodb.net/?retryWrites=true&w=majority')
db = client.teampage

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/", methods=["GET"])
def home_get():
    tmi_lists = list(db.user.find({}, {'_id': False}))
    return jsonify({'tmis': tmi_lists})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
