"""
# -*- coding: utf-8 -*-

# http://www.foxebook.net/new-release/page/pagenum


@author: Sean
"""


from pymongo import MongoClient
import os
import urllib3
import bs4
import string

dburl = 'mongodb://localhost:27017/foxbook'
proxy_url = 'http://127.0.0.1:2080'
http = urllib3.ProxyManager(proxy_url=proxy_url)
booklist =[]
count = 668  # page count


site = 'http://www.foxebook.net'  # books site

#r = http.request('GET','http://www.google.com')
#status = r.status
#data = r.data

client = MongoClient(dburl)
db = client.get_default_database()  # foxbook
collection = db.foxbooksinfo


def getDownloadUrl(item):
    href =  item['href']   
    if href.find('https') != -1:
        return 'https://'+ href.split('/https://')[1]
    else:
        return 'http://'+ href.split('/http://')[1]
    
def getbookinfo(bookurl):
    urldetail = site + bookurl
    print('urldetail: ' + urldetail)
    bookinfopage = http.request('GET',urldetail)
    soup = bs4.BeautifulSoup(bookinfopage.data,'html5lib')
    bookname = soup.select('h1')[0].text
    print('bookname: '+ bookname)
#    author = soup.select('.col-md-9 div')[2].select('a')[0].text
#    publisher = soup.select('.col-md-9 div')[3].select('a')[0].text
#    publishdate = soup.select('.col-md-9 div')[4].select('i')[0].text
#    pagecount = soup.select('.col-md-9 div')[5].select('i')[0].text
    downloadurls = list(map(getDownloadUrl,soup.select('#download')[0].select('tr a')))
    #book description
    description = soup.select('.panel-primary .panel-body')[0].text
    bookinfo = {
        'bookname':bookname,
#        'author':author,
#        'publisher':publisher,
#        'publishdate':publishdate,
#        'pagecount':pagecount,
        'downloadurls':downloadurls,
        'description':description
    }
    return bookinfo

def savebooklist(i):
    bookspage = site +'/new-release/page/' + str(i)
    all  = http.request('GET',bookspage)
    bookshtml = all.data
    soup = bs4.BeautifulSoup(bookshtml,'html5lib')
    books = soup.select('h3 a')
    booksinfo =[]
    for book in books:
        bookurl = book['href']
#        collection.insert_one({'url':bookurl})
        bookinfo = getbookinfo(bookurl)
        booksinfo.append(bookinfo)
    collection.insert_many(booksinfo)


def run():
    for i in range(132,count):
        savebooklist(i)
        print('run over page '+ str(i))

run()
        



                        
    

    