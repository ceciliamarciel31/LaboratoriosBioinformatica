# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 21:42:09 2016

@author: jfsco
"""

from Bio import SeqIO
record=SeqIO.read('our_genome.gb', 'genbank')

#features locations and type
feats={}
for i in range(1, len(record.features)):
    if record.features[i].type in feats:
        feats[record.features[i].type].append(i)
    else :
        feats[record.features[i].type]=[i]

for key in feats:
    print(key,':',feats[key])

#Notas: STS --> Sequence-tagged site, is a short sequence that has a single occurrence in the genome
#       misc_feature --> region of biological interest which cannot be described by any other feature key

#write the features in a txt file
import sys

orig_stdout = sys.stdout
f = open('features.txt', 'w')
sys.stdout = f

for i in range(1, len(record.features)):
    chaves=['db_xref', 'locus_tag', 'gene', 'protein_id', 'function', 'product', 'EC_number', 'note']
    print('\nFeature nº: %i'%(i),'\nTipo:' ,record.features[i].type)
    for chave in chaves:
        try: 
            if record.features[i].qualifiers[chave]:
                print(chave,':',record.features[i].qualifiers[chave])
        except:
            pass
sys.stdout = orig_stdout
f.close()


#abrir a tabela referente a nossa zona do genoma fornecida pelo NCBI
from collections import defaultdict
dict = defaultdict(list)
accession = 'NC_002942.5'
f = open('table.csv', 'w')
f.write('GeneID;Accession;Locus_tag;GeneName;Strand;ProteinID;ProteinName;Number of Aminoacids;Location;GO;EC;TC;Function\n')
for i in range(len(record.features)):
    if record.features[i].type == "gene":
        geneID = record.features[i].qualifiers['db_xref'][0].replace('GeneID:','')
        if ('gene' in record.features[i].qualifiers):
            geneName = record.features[i].qualifiers['gene'][0]
        else:
            geneName = 'None'
        locus = record.features[i].qualifiers['locus_tag'][0]
        dict[geneID] = [accession,locus,geneName]
    if record.features[i].type == "CDS":
        location = str(record.features[i].location.start) +':' + str(record.features[i].location.end)
        strand = record.features[i].location.strand
        proteinID = record.features[i].qualifiers['protein_id'][0]
        proteinName = record.features[i].qualifiers['product'][0]
        aminoNumber = len(record.features[i].qualifiers['translation'][0])
        if ('function' in record.features[i].qualifiers):
            function = record.features[i].qualifiers['function'][0]
        else:
            function = 'None'
        geneID = record.features[i].qualifiers['db_xref'][0].replace('GeneID:','')
        GO = 'None'
        if ('EC_number' in record.features[i].qualifiers):
            EC = record.features[i].qualifiers['EC_number'][0]
        TC = 'None'
        l = dict[geneID]
        if ('gene' in record.features[i].qualifiers):
            l[2] = record.features[i].qualifiers['gene'][0]
        l.append(str(strand))
        l.append(proteinID)
        l.append(proteinName)
        l.append(str(aminoNumber))
        l.append(location)
        l.append(GO)
        l.append(EC)
        l.append(TC)
        l.append(function)
        del dict[geneID]
        dict[geneID] = l
        geneID = str(geneID)
        f.write(geneID+';'+l[0]+';'+l[1]+';'+l[2]+';'+l[3]+';'+l[4]+';'+l[5]+';'+l[6]+';'+l[7]+';'+l[8]+';'+l[9]+';'+l[10]+';'+l[11]+'\n')
f.close()  



        