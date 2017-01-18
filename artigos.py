# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 18:11:53 2016

@author: jfsco
"""

#Neste passo vamos procurar os artigos disponiveis na PubMed relacionados com o nosso organismo,
#retornando a quantidade de artigos encontrados
from Bio import Entrez
Entrez.email = "grupo8.laboratorios@gmail.com"
handle = Entrez.egquery(term="Legionella pneumophila Philadelphia 1")
record = Entrez.read(handle)
for row in record["eGQueryResult"]:
    if row["DbName"]=="pubmed":
        z=row["Count"]

print(z)
 
#Aqui usamos a função  Bio.Entrez.esearch para obter os IDs dos artigos da PubMed
handle = Entrez.esearch(db="pubmed", term="Legionella pneumophila Philadelphia 1", retmax=z)
record = Entrez.read(handle)
idlist = record["IdList"]
print(idlist)

#Neste passo iremos proceder ao download dos registos da Medline no formato Medline e usamos
#a função Bio.Medline para os analisarmos.
from Bio import Medline
handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
records = Medline.parse(handle)

import sys
orig_stdout = sys.stdout
f = open('artigos_legionela.txt', 'w')
sys.stdout = f

records = list(records)
for record in records:
    print("Title:", record.get("TI", "?"))
    print("Authors:", record.get("AU", "?"))
    print("Source:", record.get("SO", "?"))
    print("")

sys.stdout = orig_stdout
f.close()