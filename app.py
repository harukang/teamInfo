from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://teami:itogether@cluster0.2tv5dd1.mongodb.net/?retryWrites=true&w=majority')
db = client.teampage

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/names")
def name_get():
    name_list = list(db.user.find({},{'_id':False,'num':False,'blog':False,'style':False,'hobby':False,'tmi':False, 'mbti':False,'avatar':False,'photo':False,'comment':False}))
    return jsonify({'name_lists': name_list})

@app.route("/users")
def user_get():
    user_list = list(db.user.find({}, {'_id': False}))
    return jsonify({'user_tmi': user_list})

@app.route("/users/<int:users_id>")
def profile(users_id):
   return render_template('profile.html')

@app.route('/team')
def team():
   return render_template('team.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
