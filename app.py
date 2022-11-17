from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi
app = Flask(__name__)
ca = certifi.where()
client = MongoClient('mongodb+srv://teami:itogether@cluster0.2tv5dd1.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.teampage


@app.route('/')
def home():
   return render_template('index.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route("/team/info", methods=["GET"])
def team_get():
    team_list = list(db.team.find({}, {'_id': False}))
    return jsonify({'team': team_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
