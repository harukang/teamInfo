from pymongo import MongoClient
import certifi
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

ca = certifi.where()
client = MongoClient('mongodb+srv://teami:itogether@cluster0.2tv5dd1.mongodb.net/?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.teampage


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/users/<user_id>')
def profile(user_id):
    user = db.user.find_one({'num': int(user_id)})
    avatar = user['avatar']
    name = user['name']
    mbti = user['mbti']
    style = user['style']
    blog = user['blog']
    photos = user['photo']

    return render_template('profile.html', user_id=user_id,avatar=avatar, name=name, mbti=mbti, style=style, blog=blog,
                           photos=photos)

    # @app.route('/users/<user_id>', methods=['GET'])
    # def get_profile(user_id):
    #     user = db.user.find({},{'num':user_id})
    #     print(user)

    # @app.route('/users/<user_id>/photos/<photo_id>')
    # def watch(user_id, photo_id):
    #     return render_template('watch.html')

    @app.route("/users/<user_id>/photos/<photo_id>")
    def photo_get(user_id, photo_id):
        user = db.user.find_one({'num': int(user_id)})
        return render_template('watch.html', user_id=user_id, photo_id=photo_id)

    if __name__ == '__main__':
        app.run('0.0.0.0', port=5000, debug=True)
