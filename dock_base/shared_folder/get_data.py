from pymongo import MongoClient

def get_latest_data():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['mydatabase']
    collection = db['data']
    latest_data = collection.find_one(sort=[('_id', -1)])
    client.close()
    return latest_data

# Пример использования
if __name__ == "__main__":
    data = get_latest_data()
    print(data)

