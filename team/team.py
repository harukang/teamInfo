from pymongo import MongoClient
client = MongoClient('mongodb+srv://teami:itogether@cluster0.2tv5dd1.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.teampage

doc = {
        'num' : 3,
        'name' : '이호승',
        'blog': 'https://velog.io/@juwalove7',
        'mbti': 'ISTJ',
        'style': '질문대마왕',
        'profile': '/teaminfo/image/seung.png',
        'hobby': '운동'
    }

db.user.insert_one(doc)