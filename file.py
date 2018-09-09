# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 19:10:45 2018

@author: Sean
"""

import os


path = os.path.abspath('.')
filename = 'file.txt'

filepath = os.path.join(path,filename)

with open(filepath,'wt') as f:
    f.write('Hello\n')
    


    
