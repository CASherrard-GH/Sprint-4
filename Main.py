#Create a Mongo Database and name it Data Tracker.
#Add your SPRINT 3 products file to MongoDB you just created.
#Create a collection for your top 3 products in MongoDB.
#Insert multiple documents into your collections in question (3)
#Implement a descending sort to your data in MongoDB.
#Delete 2 brands from your collection of top 3 products.
#Update 1 product and its brands from your collection you created in question (3).
#Track (Search/Filter) for the least 5 brands in your products.
#Save your MongoDB data and code to GitHub
#Make your work accessible to your team members on GitHub.

import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://user_2001:123@cluster0.qnjpq.mongodb.net/Data_Tracker?retryWrites=true&w=majority")
database = cluster["Data_Tracker"]
collection = database["Items|Ranks"]

post_chips = {"_id": 1, "Simba" : 7, "Lays": 4}
post_cooldrinks = {"_id": 2, "Coke": 1, "Fanta" : 11}
post_chocolates = {"_id": 3 ,"Cadbury": 5, "Tex": 6}
post_pies = {"_id": 4, "Pepper Steak": 3, "Chicken": 4}
post_fruit = {"_id": 5, "Pear" : 5, "Apple" : 1, "Orange": 2}
post_cupcakes = {"_id": 6, "Vanilla" : 4, "Chocolate": 2}
post_veggies = {"_id": 7, "Spinach" : 13, "Cabbage": 12}

#database.collection.find({"_id": {"$gt": 1}}).sort([("_id", 1), ("_id", -1)]) #$gt selects those documents where the value of the field is greater than (i.e. >) the specified value.
database.collection.find( {"_id": 2 } )



collection.insert_many([post_chips, post_chocolates, post_cooldrinks, post_cupcakes, post_fruit, post_pies, post_veggies])
