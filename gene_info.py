#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#código do grupo 1

from Bio import SeqIO
import re


def generate_GeneInfo(source, begin_locus, end_locus):
    dump = []
    i = 0
    records = SeqIO.parse(open(source), "genbank");
    ids = open("file_blast.fasta","w")
    regex = r'(?<=lpg)([0-9]*?)(?=$)'
    dump.append("GeneID|"+"Accession Number|"+"Locus Tag|"+"Gene|"+"Strand|"+"Protein ID(NCBI)|"+"Function|"+"Protein Name"+"\n")
    for r in records:
        for a in r.features:
            if i >= begin_locus and a.type == "CDS" and 'gene' in a.qualifiers.keys() and 'function' in a.qualifiers.keys():  #so apanha os que tem gene
                dump.append(str(a.qualifiers['db_xref'][0][7::])+"|NC_002942.5|"+str(a.qualifiers['locus_tag'][0])+"|"+str(a.qualifiers['gene'][0])+"|"+str(a.strand)+"|"+str(a.qualifiers['protein_id'][0])+"|"+str(a.qualifiers['function'][0])+"|")
                if a.qualifiers['product'][0] == "hypothetical protein":
                    dump.append(str(a.qualifiers['product'][0])+" "+str(a.qualifiers['locus_tag'][0]))
                else:
                     dump.append(str(a.qualifiers['product'][0]))
                ids.write(">"+str(a.qualifiers['db_xref'][0][7::])+"\n")
                ids.write(str(a.qualifiers['translation'][0]))
                ids.write("\n")
                dump.append("\n")
            elif i >= begin_locus and a.type == "CDS" and 'function' in a.qualifiers.keys():
                dump.append(str(a.qualifiers['db_xref'][0][7::])+"|NC_002942.5|"+str(a.qualifiers['locus_tag'][0])+"|"+"-"+"|"+str(a.strand)+"|"+str(a.qualifiers['protein_id'][0])+"|"+str(a.qualifiers['function'][0])+"|")
                if a.qualifiers['product'][0] == "hypothetical protein":
                    dump.append(str(a.qualifiers['product'][0])+" "+str(a.qualifiers['locus_tag'][0]))
                else:
                     dump.append(str(a.qualifiers['product'][0]))
                ids.write(">"+str(a.qualifiers['db_xref'][0][7::])+"\n")
                ids.write(str(a.qualifiers['translation'][0]))
                ids.write("\n")
                dump.append("\n")            
            elif i >= begin_locus and a.type == "CDS" and 'gene' in a.qualifiers.keys():
                dump.append(str(a.qualifiers['db_xref'][0][7::])+"|NC_002942.5|"+str(a.qualifiers['locus_tag'][0])+"|"+str(a.qualifiers['gene'][0])+"|"+str(a.strand)+"|"+str(a.qualifiers['protein_id'][0])+"|"+"-|")
                if a.qualifiers['product'][0] == "hypothetical protein":
                    dump.append(str(a.qualifiers['product'][0])+" "+str(a.qualifiers['locus_tag'][0]))
                else:
                     dump.append(str(a.qualifiers['product'][0]))
                ids.write(">"+str(a.qualifiers['db_xref'][0][7::])+"\n")
                ids.write(str(a.qualifiers['translation'][0]))
                ids.write("\n")
                dump.append("\n")
                
            elif i >= begin_locus and a.type == "CDS":
                dump.append(str(a.qualifiers['db_xref'][0][7::])+"|NC_002942.5|"+str(a.qualifiers['locus_tag'][0])+"|"+"-"+"|"+str(a.strand)+"|"+str(a.qualifiers['protein_id'][0])+"|"+"-|")
                if a.qualifiers['product'][0] == "hypothetical protein":
                    dump.append(str(a.qualifiers['product'][0])+" "+str(a.qualifiers['locus_tag'][0]))
                else:
                     dump.append(str(a.qualifiers['product'][0]))
                ids.write(">"+str(a.qualifiers['db_xref'][0][7::])+"\n")
                ids.write(str(a.qualifiers['translation'][0]))
                ids.write("\n")
                dump.append("\n")
            if a.type == "CDS":
                lpg = (re.search(regex,a.qualifiers['locus_tag'][0]))
                if not lpg == None:
                    lpg = int(lpg.group(0))
                    i += 1
            if a.type =="CDS" and lpg == end_locus:
                break                            
    xnor = open("dump.csv","w");
    for d in dump:
        xnor.write(d)        
    
    records.close();
    xnor.close();

#desde o locus 1618 até ao 1848
generate_GeneInfo("our_genome.gb",1618,1848)    

