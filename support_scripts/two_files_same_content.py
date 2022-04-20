# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 19:47:01 2022

@author: Thanasis
"""

#!/usr/bin/env python3
import sys
from os import listdir

def readfile(path):
    with open(path, 'rb') as f:
        return f.read()
mypath = r'C:\Users\Thanasis\Documents\nand2tetris\nand2tetris\projects\02'
contentscmp = []
contentsout = []
contentscmp = [(mypath+'\\'+fname) for fname in listdir(mypath) if ('.cmp' in fname )]
contentsout = [(mypath+'\\'+fname) for fname in listdir(mypath) if ( '.out' in fname)]
names = [ fname.split('.')[0] for fname in contentsout  ]
#print(len(contentscmp),len(contentsout), sep = '\n')
print(* [readfile(name + '.cmp')==readfile(name + '.out') \
       for name in names ], sep = '\n')
sys.exit(all([readfile(name + '.cmp')==readfile(name + '.out') \
       for name in names ]))