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

post_chips = {"_id": 1, "Brand": "Simba", "Rank": 7}
post_cooldrinks = {"_id": 2, "Brand": "Coke", "Rank": 1}
post_chocolates = {"_id": 3, "Brand": "Cadbury", "Rank": 9}
post_pies = {"_id": 4, "Brand": "Pepper Steak", "Rank": 3}
post_fruit = {"_id": 5, "Brand": "Pear", "Rank": 5}
post_cupcakes = {"_id": 6, "Brand": "Vanilla", "Rank": 4}
post_veggies = {"_id": 7, "Brand": "Spinach", "Rank": 13}
post_chips2 = {"_id": 8, "Brand": "Lays", "Rank": 4}
post_cooldrinks2 = {"_id": 9, "Brand": "Fanta", "Rank": 11}
post_chocolates2 = {"_id": 10, "Brand": "Tex", "Rank":  6}
post_pies2 = {"_id": 11, "Brand": "Chicken", "Rank": 4}
post_fruit2 = {"_id": 12, "Brand": "Apple", "Rank": 1}
post_fruit3 = {"_id": 13, "Brand": "Orange", "Rank": 2}
post_cupcakes2 = {"_id": 14, "Brand": "Chocolate", "Rank": 2}
post_veggies2 = {"_id": 15, "Brand": "Cabbage", "Rank": 12}



collection.insert_many([post_chips, post_chips2, post_cooldrinks, post_cooldrinks2, post_chocolates, post_chocolates2, post_pies, post_pies2, post_fruit, post_fruit2, post_fruit3, post_cupcakes, post_cupcakes2, post_veggies, post_veggies2])




query = { "Rank": 13 }

prnt = collection.find(query)
for i in prnt:
  print(i)

query = { "Rank": 12 }

prnt = collection.find(query)

for i in prnt:
  print(i)
 
    
query = { "Rank": 11 }

prnt = collection.find(query)

for i in prnt:
  print(i)
  
query = { "Rank": 7 }

prnt = collection.find(query)

for i in prnt:
  print(i)
  

  
query = { "Rank": 5 }

prnt = collection.find(query)

for i in prnt:
  print(i)