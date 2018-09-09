# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 23:32:36 2018


pyMongo API
https://api.mongodb.com/python/current/

@author: Sean
"""


from pymongo import MongoClient
import os
import urllib3
import bs4

url = 'mongodb://localhost:27017/'
proxy_url = 'http://127.0.0.1:2080'
http = urllib3.ProxyManager(proxy_url=proxy_url)
booklist =[]
count = 768
#r = http.request('GET','http://www.google.com')
#status = r.status
#data = r.data
client = MongoClient(url)
db = client.books
collection = db.bookurl

def savebooklist(booklist,i):
    allitebooks = 'http://www.allitebooks.com/page/'+ str(i)
    all  = http.request('GET',allitebooks)
    alldata = all.data
    soup = bs4.BeautifulSoup(alldata,'html5lib')
    books = soup.select('h2 a')
    for book in books:
        bookurl = book['href']
        collection.insert_one({'url':bookurl})
        
#for i in range(1,count):
#    getbooklist(booklist,i)
        
        
def getbookurl():
    
        

    
    
