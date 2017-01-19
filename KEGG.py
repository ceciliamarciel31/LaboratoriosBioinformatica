# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 16:41:59 2017

@author: jfsco
"""

from Bio.KEGG import REST, Enzyme
import xlsxwriter as xls

metabolic_networks=[]
workbook = xls.Workbook('metabolic_proteins_python.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 20)
bold=workbook.add_format({'bold':True})

lpgs=['lpg1619', 'lpg1630', 'lpg1631', 'lpg1632', 'lpg1637', 'lpg1643', 'lpg1646', 'lpg1649', 'lpg1650', 'lpg1651', 'lpg1652', 'lpg1664', 'lpg1669', 'lpg1671', 'lpg1672', 'lpg1673', 'lpg1674', 'lpg1675', 'lpg1676', 'lpg1677', 'lpg1678', 'lpg1690', 'lpg1696', 'lpg1699', 'lpg1700', 'lpg1706', 'lpg1707', 'lpg1708', 'lpg1712', 'lpg1721', 'lpg1722', 'lpg1723', 'lpg1726', 'lpg1734', 'lpg1739', 'lpg1746', 'lpg1748', 'lpg1753', 'lpg1757', 'lpg1767', 'lpg1774', 'lpg1775', 'lpg1777', 'lpg1799', 'lpg1808', 'lpg1811', 'lpg1818', 'lpg1821', 'lpg1824', 'lpg1825', 'lpg1827', 'lpg1828', 'lpg1829', 'lpg1830', 'lpg1831', 'lpg1838', 'lpg1839', 'lpg1840', 'lpg1843', 'lpg1846', 'lpg1847']

worksheet.write(0, 0, 'Locus tag', bold)
worksheet.write(0, 1, 'Defenition', bold)
worksheet.write(0, 2, 'EC number', bold)
worksheet.write(0, 3, 'KEGG ortholog', bold)
worksheet.write(0, 4, 'Pathways', bold)
worksheet.write(0, 5, 'Data Base Links', bold)
i=1
for lpg in lpgs:
    request=REST.kegg_get("lpn:%s" %lpg)
    open("%s.txt" %lpg, "w").write(request.read())
    records=Enzyme.parse(open("%s.txt" %lpg))
    record=list(records)[0]
    worksheet.write(i, 0, lpg)
    for line in open("%s.txt" %lpg):
        if line[0:10]=='DEFINITION':
            worksheet.write(i, 1, line[20::])
        if line[0:9]=='ORTHOLOGY':
            a=line.find('EC:')
            if a!=-1:
                worksheet.write(i, 3, line[10:a-1])
                worksheet.write(i, 2, line[a-1::])
            else :
                worksheet.write(i, 3, line[10::])            
    worksheet.write(i, 4, str(record.pathway))
    metabolic_networks.append((lpg, record.pathway))
    worksheet.write(i, 5, str(record.dblinks))
    i+=1
    
    
workbook.close()

import sys
orig_stdout = sys.stdout
f = open('metabolic_networks.txt', 'w')
sys.stdout = f

for net in metabolic_networks:
    print(net)

sys.stdout = orig_stdout
f.close()