import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://......:......@...cluster-......mongodb.net/...............")
db = cluster["test_db"]
collection = db["test_collection"]

#post1 = {"_id": 31783617, "name": "Pupilu", "score": 10}
#post1 = {"_id": 31783618, "name": "Pupilupi", "score": 9}
#post2 = {"_id": 31783619, "name": "Pupipapi", "score": 11}

#collection.insert_many(post)
#collection.insert_many([post1, post2])

results = collection.find({"name":"Pupilupi"})

for result in results:
    print(result)

resultOne = collection.find_one({"score":11})

print(resultOne["_id"])

resultsAll = collection.find({})

for x in resultsAll:
    print(x)

#post3 = {"_id": 0, "name": "Pingi", "score": 100}
#collection.insert_one(post3)

#resultsDel = collection.delete_one({"_id":0})

#resultsDelAll = collection.delete_many({})

resultsUpdate = collection.update_one({"_id":0}, {"$set":{"name":"Piggy"}})

postCount = collection.count_documents({})
print(postCount)
