# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 22:48:42 2017

@author: jfsco
"""

import xlsxwriter as xls

workbook = xls.Workbook('func.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 20)
bold=workbook.add_format({'bold':True})

i=0
j=0
metabolic_p=[]
transp_p=[]
ft_p=[]

for line in open('funcoes.txt', 'r'):
    if line[0:3]=='lpg':
        if 'Sem função conhecida' in line:
            c='red'
        elif 'Metabolism' in line:
            c='blue'
            metabolic_p.append(line[0:7])
        elif 'Transport' in line:
            c='green'
            transp_p.append(line[0:7])
        elif 'Transcription factor' in line:
            c='yellow'
            ft_p.append(line[0:7])
        elif 'Translation' in line:
            c='white'
        elif 'Chemotaxis' in line:
            c='orange'
        elif 'Replication and Repair' in line:
            c='brown'
        elif 'Toxin production' in line:
            c='purple'
        elif 'DNA/RNA degradation' in line:
            c='pink'
        elif 'Detoxification' in line:
            c='silver'
        elif 'secretion' in line:
            c='navy'
        elif 'Biodegradation of Xenobiotics' in line:
            c='gray'
        elif 'Viral functions' in line:
            c='lime'
        elif 'Signal transduction' in line:
            c='magenta'
        else :
            c=input(line[31::]+'Cor: ')
        color=workbook.add_format({'bg_color': c})
        worksheet.write(j, i, line[0:7], color)
        i+=1
        if i==15:
            j+=1
            i=0

worksheet.write(19, 0, 'Lengenda:')
worksheet.write(20, 0, 'Cor:')
worksheet.write(20, 1, 'Função:')
worksheet.write(21, 0, '', workbook.add_format({'bg_color': 'red'}))
worksheet.write(21, 1, 'Sem função conhecida!')
worksheet.write(22, 0, '', workbook.add_format({'bg_color': 'blue'}))
worksheet.write(22, 1, 'Metabolismo')
worksheet.write(23, 0, '', workbook.add_format({'bg_color': 'green'}))
worksheet.write(23, 1, 'Transporte')
worksheet.write(24, 0, '', workbook.add_format({'bg_color': 'yellow'}))
worksheet.write(24, 1, 'Fator de transcrição')
worksheet.write(25, 0, '', workbook.add_format({'bg_color': 'white'}))
worksheet.write(25, 1, 'Tradução')
worksheet.write(26, 0, '', workbook.add_format({'bg_color': 'orange'}))
worksheet.write(26, 1, 'Quimiotaxia')
worksheet.write(27, 0, '', workbook.add_format({'bg_color': 'brown'}))
worksheet.write(27, 1, 'Replicação e Reparação')
worksheet.write(28, 0, '', workbook.add_format({'bg_color': 'purple'}))
worksheet.write(28, 1, 'Produção de toxinas')
worksheet.write(29, 0, '', workbook.add_format({'bg_color': 'pink'}))
worksheet.write(29, 1, 'Degradação do DNA/RNA')
worksheet.write(30, 0, '', workbook.add_format({'bg_color': 'silver'}))
worksheet.write(30, 1, 'Detoxificação')
worksheet.write(31, 0, '', workbook.add_format({'bg_color': 'navy'}))
worksheet.write(31, 1, 'Secreção')
worksheet.write(32, 0, '', workbook.add_format({'bg_color': 'gray'}))
worksheet.write(32, 1, 'Biodegradação de Xenobióticos')
worksheet.write(33, 0, '', workbook.add_format({'bg_color': 'lime'}))
worksheet.write(33, 1, 'Funções Virais')
worksheet.write(34, 0, '', workbook.add_format({'bg_color': 'magenta'}))
worksheet.write(34, 1, 'Tradução de sinais')
workbook.close()

    
