# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 13:31:20 2016


"""

from Bio import SeqIO 

record = SeqIO.read('our_genome.gb', 'genbank')

from collections import defaultdict
dict = defaultdict(list)
accession = 'NC_002942.5'
f = open('table2.csv', 'w')
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
        else:
            EC = 'None'
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
