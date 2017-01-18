#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#código do grupo 1

from Bio import ExPASy
from Bio import SeqIO
from Bio import SwissProt
import requests
import re


l = open("blast_filtrado.txt","r")
c = []
regex = '<keyword id=".*">(.*)</.*>'
regex1 = '<property type="term" value="(.*)"/>'
inf = open("blast_analise.csv","w")
for x in l.readlines():
    c.append(x)

for un in c:
    record = requests.get("http://www.uniprot.org/uniprot/"+un.replace("\n","")+".xml")  
    try:
        inf.write(un)
        inf.write("KW:")
        inf.write(','.join(re.findall(regex,record.text)))
        inf.write("\n")
        inf.write("GO:")
        inf.write(','.join(re.findall(regex1,record.text)))
        inf.write("\n\n")
    except Exception as e:
        print(e)
        
inf.close()
l.close()        
