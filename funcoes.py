# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 16:58:17 2017

@author: jfsco
"""

from Bio import SeqIO

record = SeqIO.read("our_genome.gb", "gb")
funcoes=[]
fun_conhecida = 0
fun_nao_conhecida = 0
for feature in record.features:
    if feature.type == "CDS":
        if 'function' in feature.qualifiers:
            funcoes.append((feature.qualifiers["locus_tag"], feature.qualifiers["protein_id"], feature.qualifiers["function"]))
            fun_conhecida += 1
        else :
            funcoes.append((feature.qualifiers["locus_tag"], feature.qualifiers["protein_id"], 'Sem função conhecida!'))
            fun_nao_conhecida += 1
        
import sys
orig_stdout = sys.stdout
f = open('funcoes.txt', 'w')
sys.stdout = f

print("Genes/proteinas e respetivas funções:\n")
print("Genes/proteinas com funções conhecidas:", fun_conhecida)
print("Genes/proteinas com funções desconhecidas:", fun_nao_conhecida, "\n")
print("Gene    || Proteina        --> funcao")
for fun in funcoes:
    print(fun[0][0], "||",fun[1], "-->", fun[2])

sys.stdout = orig_stdout
f.close()
    