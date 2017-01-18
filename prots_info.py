# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:33:38 2016

@author: jfsco
"""

from Bio import ExPASy
from Bio import SwissProt
codigos=open('prots_ids.txt', 'r')
codes=codigos.read()
cdd=codes.split('\n')

import sys
orig_stdout = sys.stdout
f = open('prots_info.txt', 'w')
sys.stdout = f

for code in cdd:
    try:
        handle2 = ExPASy.get_sprot_raw(code)
        while True:
            try:
                record = SwissProt.read(handle2)
                print("\n\n****Informacao sobre a proteina: %s****\n" %code)
                print("\nNome: %s\n" %record.entry_name)
                print("Classe: %s\n" %record.data_class)
                print("Tipo de molecula: %s\n" %record.molecule_type)
                print("Tamanho da sequencia: %s\n" %record.sequence_length)
                print("Codigo de Accesso: %s\n" %record.accessions)
                print("Criado: %s\n"% str(record.created))
                print("Descricao: %s\n" %record.description)
                print("Nome do gene: %s\n" %record.gene_name)
                print("Organismo: %s\n" %record.organism)
                print("Classificacao do Organismo: %s\n" %record.organism_classification)
                print("ID da taxonomia: %s\n" %record.taxonomy_id)
                print("Comentarios: %s\n" %record.comments)
                print("Palavras-chave: %s\n" %record.keywords)
                print("Caracteristicas: %s\n" %record.features)
                print("Sequencia: %s\n" %str(record.sequence))
                print("Informação da sequência: %s\n" %str(record.seqinfo))
                print("\n****Referencias sobre a proteina****\n")
                for ref in record.references:
                    print("Numero: %s\n" %ref.number)
                    print("Posicao: %s\n" %ref.positions)
                    print("Comentarios: %s\n" %ref.comments)
                    print("Referencias: %s\n" %ref.references)
                    print("Autores: %s\n" %ref.authors)
                    print("Titulo: %s\n" %ref.title)
                    print("Localizacao: %s\n\n" %ref.location)
                    print('***********************************')
                break
            except Exception:
                break
    except :
        pass
    
sys.stdout = orig_stdout
f.close()
codigos.close()
