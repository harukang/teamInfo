from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.kswkoyd.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route("/", methods=["GET"])
def home():
   tmi_list = list(db.user.find({}, {'_id': False}))
   return jsonify({'orders': tmi_list})
   print(tmi_list)

