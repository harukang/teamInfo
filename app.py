from pymongo import MongoClient
import  gridfs

def mongo_conn():
    try:
        conn = MongoClient(host='127.0.01', port=27017)
        print("MongoDB connection", conn)
        return conn.grid_file
    except Exception as e:
        print("Error in connection", e)

db = mongo_conn()
name = 'book.pdf'
file_location = "/home/uddav/Documents/projects/" + name
file_data = open(file_location, "rb")
data = file_data.read()
fs = gridfs.GridFS(db)
fs.put(data, filename = name)
print("upload complete")

data = db.fs.files.fine_one({'filename':name})
my_id = data['_id']
outputdata = fs.get(my_id).read()
download_location = "/home/uddav/Documents/projects/download/" + name
output = open(download_location, "wb")
output.write(outputdata)
output.close()
print("download complete")