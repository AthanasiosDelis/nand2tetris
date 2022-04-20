# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 19:47:01 2022

@author: Thanasis
"""

#!/usr/bin/env python3
import sys
from os import listdir
from os.path import isfile, join

def readfile(path):
    with open(path, 'rb') as f:
        return f.read()
mypath = r'C:\Users\Thanasis\Documents\nand2tetris\nand2tetris\projects\01'
contentscmp = []
contentsout = []
contentscmp = [(mypath+r'\\'+fname) for fname in listdir(mypath) if ('.cmp' in fname )]
contentsout = [(mypath+r'\\'+fname) for fname in listdir(mypath) if ( '.out' in fname)]
print(len(contentscmp),len(contentsout), sep = '\n')
#print(, sep = '\n')
sys.exit(all([readfile(contentout)==readfile(contentcmp) \
       for contentout,contentcmp in zip(contentscmp,contentsout)]))