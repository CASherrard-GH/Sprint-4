import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://user_2001:123@cluster0.qnjpq.mongodb.net/Data_Tracker?retryWrites=true&w=majority")
database = cluster["Top_3"]
collection = database["Products"]

post_cooldrink = {"_id": 1, "Catagory": "Cooldrink", "Brand": "Coke", "Rank": 1}
post_fruit = {"_id": 2, "Catagory": "Fruit", "Type": "Apple", "Rank": 1}
post_fruit2 =  {"_id": 3, "Catagory": "Fruit", "Type": "Orange", "Rank": 2}


  
collection.insert_many([post_cooldrink, post_fruit, post_fruit2])

mysort = collection.find().sort("_id", -1)
for x in mysort:
  print(x)
  
dltquery1 = { "_id": 1 }

collection.delete_one(dltquery1)


dltquery2 = { "_id": 2 }

collection.delete_one(dltquery2)



updatequery = {"Rank": 2}
updatevalues = { "$set": {"Rank": "1"}}


collection.update_one(updatequery, updatevalues)

for j in collection.find():
  print(j)