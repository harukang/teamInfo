from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://teami:itogether@cluster0.2tv5dd1.mongodb.net/?retryWrites=true&w=majority')
db = client.teampage


@app.route('/')
def home():
   return render_template('index.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route("/team/info", methods=["GET"])
def team_get():
    print('실행됨')
    team_list = list(db.team.find({}, {'_id': False}))
    return jsonify({'team': team_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
