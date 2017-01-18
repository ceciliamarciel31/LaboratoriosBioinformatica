
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
