import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://user_2001:123@cluster0.qnjpq.mongodb.net/Data_Tracker?retryWrites=true&w=majority")
database = cluster["Top_3"]
collection = database["Products"]

post_cooldrink = {"_id": 1, "Catagory": "Cooldrink", "Brand": "Coke", "Rank": 1}
post_fruit = {"_id": 2, "Catagory": "Fruit", "Type": "Apple", "Rank": 1}
post_fruit2 =  {"_id": 3, "Catagory": "Fruit", "Type": "Orange", "Rank": 2}


collection.insert_many([post_cooldrink, post_fruit, post_fruit2])
