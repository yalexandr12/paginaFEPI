from flask import Flask
from pymongo import MongoClient
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    client = MongoClient('mongo', 27017)
    db = client.mydatabase
    collection = db.mycollection
    collection.insert_one({'name': 'John'})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')



