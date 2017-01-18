# -*- coding: utf-8 -*-

#código do grupo 1

from Bio.Blast import NCBIXML
from Bio       import SeqIO
from Bio.Blast import NCBIWWW
import re as reg


records = NCBIXML.parse(open("results.xml","r"))
regex = r'(?<=\|sp\|).*'

dump = open("blast_verify.csv","w")
for re in records:
    dump.write(re.query+"@")
    for alignment in re.alignments:
        for hsp in alignment.hsps:                     
            dump.write(reg.search(regex,str(alignment.title)).group().replace("|","@")+"@"+str(hsp.expect)+"@"+str(hsp.score)+"@"+str(hsp.align_length)+"\n")
            break;
        break;            
    dump.write('\n')