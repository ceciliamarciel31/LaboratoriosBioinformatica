# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 17:46:27 2016

@author: Utilizador
"""

from Bio import SeqIO
from Bio import Entrez

# aceder ao NCBI e guardar o ficheiro correspondente
# a zona do genoma

Entrez.email = 'grupo8.laboratorios@gmail.com'
handle=Entrez.efetch(db='nucleotide', rettype='gb', retmode='text', id='NC_002942.5', seq_start='1786151', seq_stop='2072130')
our_genome=SeqIO.read(handle, 'gb')
SeqIO.write(our_genome, 'our_genome.gb', 'gb')
handle.close ()

#guardar a sequencia num txt
#gravar a sequencia num txt
Dfile= open('our_sequence.txt', 'w')
Dfile.write(str(our_genome.seq)) 
Dfile.close()

