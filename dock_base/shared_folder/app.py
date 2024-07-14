from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['data']

@app.route('/data', methods=['POST'])
def save_data():
    data = request.json
    collection.insert_one(data)
    return jsonify({"status": "success"}), 201

@app.route('/data', methods=['GET'])
def get_data():
    latest_data = collection.find_one(sort=[('_id', -1)])
    return jsonify(latest_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
