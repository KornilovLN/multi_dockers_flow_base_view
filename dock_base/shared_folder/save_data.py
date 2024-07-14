from pymongo import MongoClient

def save_to_mongodb(data):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['mydatabase']
    collection = db['data']
    collection.insert_one(data)
    client.close()

# Пример использования
if __name__ == "__main__":
    sample_data = {"sensor": "temperature", "value": 25.5}
    save_to_mongodb(sample_data)
