# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 22:33:14 2016

@author: jfsco
"""

from Bio.PDB import PDBList, PDBParser

#Apenas foi encontrada uma proteina com registo na base de dados PDB 
#para fazer par multiplas proteinas bastava fazer um loop com os ids da pdb das proteinas
p = PDBParser(PERMISSIVE=1)
structure_id = "5t2x"
filename = "5t2x.pdb"
s = p.get_structure(structure_id, filename)
pdbl = PDBList()
pdbl.retrieve_pdb_file('5T2X')

import sys
orig_stdout = sys.stdout
f = open('pdb_info.txt', 'w')
sys.stdout = f
print("****Analise da estrutura 5T2X****\n")
print("Palavras Chave: %s" %s.header['keywords'])
print("Nome do Organismo: %s" %s.header['name'])
print("Cabecalho: %s" %s.header['head'])
print("Data da deposicao: %s" %s.header['deposition_date'])
print("Data da publicacaos: %s" %s.header['release_date'])
print("Metodo usado: %s" %s.header['structure_method'])
print("Resolucao: %s" %s.header['resolution'])
print("Referencia da estrutura: %s" %s.header['structure_reference'])
print("Referencia de artigo: %s" %s.header['journal_reference'])
print("Autor: %s" %s.header['author'])
print("Composto: %s\n" %s.header['compound'])
sys.stdout = orig_stdout
f.close()