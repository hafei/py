# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 23:32:36 2018

@author: Sean
"""



import os
import urllib3
import bs4


proxy_url = 'http://127.0.0.1:2080'
http = urllib3.ProxyManager(proxy_url=proxy_url)
booklist =[]
count = 768
#r = http.request('GET','http://www.google.com')
#status = r.status
#data = r.data

def getbooklist(booklist,i):
    allitebooks = 'http://www.allitebooks.com/page/'+ str(i)
    all  = http.request('GET',allitebooks)
    alldata = all.data
    soup = bs4.BeautifulSoup(alldata,'lxml')
    books = soup.select('h2 a')
    for book in books:
        booklist.append(book['href'])
        
for i in range(1,count):
    getbooklist(booklist,i)
    
    
