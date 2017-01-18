# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 17:23:27 2016

@author: jfsco
"""

from Bio.SwissProt import KeyWList

handle = open("prots_uniprot.txt")
records = KeyWList.parse(handle)
codes = [] 
review = open("nossas_prots.txt", "w")   
for record in records:
    review.write("\n"+record['ID']+"\n")
    review.write("\n"+record['DE']+"\n")
    codes.append(record['AC'][:-1])
handle.close()
review.close()

import sys
orig_stdout = sys.stdout
f = open('prots_ids.txt', 'w')
sys.stdout = f
for code in codes:
    print(code)
    
sys.stdout = orig_stdout
f.close()