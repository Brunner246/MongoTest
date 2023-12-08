from typing import List, Dict

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['exampleDB']


def main():
    mydb = db["mydatabase"]
    mycol = mydb["customers"]

    mylist = create_sample_data()

    for data in mylist:
        # Use upsert to insert or update based on the _id value
        mycol.update_one({"_id": data["_id"]}, {"$set": data}, upsert=True)

    for document in mycol.find():
        print(document)


if __name__ == '__main__':
    main()


def create_sample_data() -> List[Dict]:
    return [
        {"_id": 1, "name": "John", "address": "Highway 37"},
        {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
        {"_id": 3, "name": "Amy", "address": "Apple st 652"},
        {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
        {"_id": 5, "name": "Michael", "address": "Valley 345"},
        {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
        {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
        {"_id": 8, "name": "Richard", "address": "Sky st 331"},
        {"_id": 9, "name": "Susan", "address": "One way 98"},
        {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
        {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
        {"_id": 12, "name": "William", "address": "Central st 954"},
        {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
        {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
    ]
