from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
# from pymongo import MongoClient
import certifi
ca = certifi.where()
# client = MongoClient('mongodb+srv://test:sparta@sparta.84x1qtl.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
# db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/users/<username>')
def profile(username):
    return render_template('profile.html')

@app.route('/users/<username>/photos/<photo_id>')
def watch(username,photo_id):
    return render_template('watch.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)