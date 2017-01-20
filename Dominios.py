# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 17:32:29 2017

@author: jfsco
"""

import sys
orig_stdout = sys.stdout
f = open('dominios.txt', 'w')
sys.stdout = f

lpgs=[]
for line in open("prots_uniprot.txt", "r"):
    if line[0:2]=='GN' and line[23:26]=='lpg':
        print('-->'+line[23:30])
        lpgs.append(line[23:30])
    if "DOMAIN" in line:
        print(line[5::])
    
sys.stdout = orig_stdout
f.close()

no_func_lpgs=[]
for line in open('funcoes.txt', 'r'):
    if line[0:7] in lpgs and line[31:52]=='Sem função conhecida!':
        no_func_lpgs.append(line[0:7])

string=''
for line in open('dominios.txt', 'r'):
    if line[0:3]=='-->':
        string+='||'
        string+=line
    else :
        string+=line
 
a=string.replace('\n', ' ')
b=a.split('||')
doms=[]
for i in range(len(b)):
    if b[i][3:10] in no_func_lpgs and len(b[i])>12:
        doms.append(b[i])
        
import xlsxwriter as xls

workbook = xls.Workbook('no_func_lpgs_domains.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 20)

worksheet.write(0, 0, 'Locus tag')
worksheet.write(0, 1, 'Dominios')
i=1
for k in range(len(doms)):
    worksheet.write(i, 0, doms[k][3:10])
    worksheet.write(i, 1, doms[k][11::])
    i+=1

workbook.close()
        
        
      
        

        