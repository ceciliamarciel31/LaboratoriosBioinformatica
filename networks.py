# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 23:16:38 2017

@author: jfsco
"""

from re import finditer

networks={}
for line in open('metabolic_networks.txt', 'r'):
    a=[m.start() for m in finditer('lpn', line)]
    for n in a:
        if line[n:n+8] in networks:
            networks[line[n:n+8]].append(line[2:9])
        else :
            networks[line[n:n+8]]=[line[2:9]]

import sys
orig_stdout = sys.stdout
f = open('pathways.txt', 'w')
sys.stdout = f

print('Pathway | number of proteins involved')
for net in networks:
    n=0
    for i in networks[net]:
        n+=1
    print(net, n)

sys.stdout = orig_stdout
f.close()