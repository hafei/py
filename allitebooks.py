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

site = 'http://www.allitebooks.com/'
count = 776

#db
dburl = 'mongodb://localhost:27017/allitebooks'
proxy_url = 'http://127.0.0.1:2080'
http = urllib3.ProxyManager(proxy_url=proxy_url)

client = MongoClient(dburl)
db = client.get_database()
collection = db.booksinfo

def savebooklist(i):
    allitebooks = site + 'page/'+ str(i)
    all  = http.request('GET',allitebooks)
    alldata = all.data
    soup = bs4.BeautifulSoup(alldata,'html5lib')
    books = soup.select('h2 a')
    booksinfo = []
    for book in books:
        bookurl = book['href']
        bookinfo = getBookinfo(bookurl)
        booksinfo.append(bookinfo)
        
    collection.insert_many(booksinfo)
        
'''
help methods
'''
def getiteminfo(item):
    return item.text
    
def getdownloadlink(item):
    return item['href']   
'''
help methods
'''


def getBookinfo(bookurl):
    urldetail =  bookurl
    print('bookurl: ' + urldetail)
    bookinfopage = http.request('GET',urldetail)
    soup = bs4.BeautifulSoup(bookinfopage.data,'html5lib')

    #book information
    bookname = soup.select('h1')[0].text
    print('bookname: '+ bookname)
    try:
        author = list(map(getiteminfo,soup.select('.book-detail dl dt')[0].next_sibling.select('a')))
        ISBN = soup.select('.book-detail dl dt')[1].next_sibling.text
        year = soup.select('.book-detail dl dt')[2].next_sibling.text
        pages = soup.select('.book-detail dl dt')[3].next_sibling.text
        language = soup.select('.book-detail dl dt')[4].next_sibling.text
        filesize = soup.select('.book-detail dl dt')[5].next_sibling.text
        fileformat = soup.select('.book-detail dl dt')[6].next_sibling.text
        downloadlinks = list(map(getdownloadlink,soup.select('.download-links a')))
        bookinfo = {
                'bookname' : bookname,
                'bookurl': bookurl,
                'author': author,
                'ISBN': ISBN,
                'year': year,
                'pages': pages,
                'language': language,
                'filesize': filesize,
                'fileformat': fileformat,
                'downloadlinks':downloadlinks
                }
    except BaseException:
        bookinfo ={
                'bookname' : bookname,
                'bookurl': bookurl,
                'except': 'html parse error'
                }
    return bookinfo

def getAllitebooks(count):
    for i in range(21, count):
        savebooklist(i)
        print('Run over page '+str(i))

getAllitebooks(count)