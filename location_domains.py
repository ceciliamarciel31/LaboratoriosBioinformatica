# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 18:54:08 2017

@author: jfsco
"""

import sys
orig_stdout = sys.stdout
f = open('prots_location_domains.txt', 'w')
sys.stdout = f

for line in open("prots_uniprot.txt", "r"):
    if line[:2]=="AC":
        print(">"+line[5::])
    if "RecName" in line[5:13]:
        print(line[5::])
    if "SUBCELLULAR LOCATION" in line:
        print(line[9::])
    if "DOMAIN" in line:
        print(line[5::])
    
sys.stdout = orig_stdout
f.close()
