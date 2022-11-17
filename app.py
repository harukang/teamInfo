from pymongo import MongoClient
import certifi
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
ca = certifi.where()
client = MongoClient('mongodb+srv://teami:itogether@cluster0.2tv5dd1.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)

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
    return jsonify({'users': user_list})

@app.route('/team')
def team():
    return render_template('team.html')


@app.route("/team/info", methods=["GET"])
def team_get():
    team_list = list(db.team.find({}, {'_id': False}))
    return jsonify({'team': team_list})

@app.route('/users/<user_id>')
def profile(user_id):
    user = db.user.find_one({'num': int(user_id)})
    avatar = user['avatar']
    name = user['name']
    mbti = user['mbti']
    style = user['style']
    blog = user['blog']
    photos = user['photo']

    return render_template('profile.html', user_id=user_id, avatar=avatar, name=name, mbti=mbti, style=style, blog=blog,
                           photos=photos)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
