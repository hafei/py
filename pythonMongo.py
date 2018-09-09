# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 17:24:06 2018

@author: Sean
"""

from pymongo import MongoClient
import datetime
#const
url = 'mongodb://localhost:27017/'


#variable
#client = MongoClient()

client = MongoClient(url)

db = client.books
collection = db.bookurl


#post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.datetime.utcnow()}
#
#post_id = collection.insert_one(post).inserted_id
#
#print(post_id)



