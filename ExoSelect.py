import pandas as pd

listexo = []
f = open("Projet NSI.txt", "r")
data = f.read()
data_sep = str(data).split('\n')

Deltoide = True
Biceps = True
Biceps_Brachial = True
muscle_des_avants_bras = True
for x in range(len(str(data).split('\n'))):
    if 'Deltoïde' in str(data_sep[x]) and Deltoide:
        exo = str(data_sep[x]).split(';')
        if str(exo[5]) == "Pas de matérielle":
            if str(exo[1,3]) not in str(listexo):
                listexo.append(exo[1,3])
    
    if 'Biceps' in str(data_sep[x]) and Biceps:
        exo = str(data_sep[x]).split(';')
        if str(exo[5]) == "Pas de matérielle":
            if str(exo[1,3]) not in str(listexo):
                listexo.append(exo[1,3])
    
    if 'Brachial' in str(data_sep[x]) and Brachial:
        exo = str(data_sep[x]).split(';')
        if str(exo[5]) == "Pas de matérielle":
            if str(exo[1,3]) not in str(listexo):
                listexo.append(exo[1,3])
    
    if 'Biceps_Brachial' in str(data_sep[x]) and Biceps_Brachial:
        exo = str(data_sep[x]).split(';')
        if str(exo[5]) == "Pas de matérielle":
            if str(exo[1,3]) not in str(listexo):
                listexo.append(exo[1,3])
                
    if 'muscle_des_avants_bras' in str(data_sep[x]) and muscle_des_avants_bras:
        exo = str(data_sep[x]).split(';')
        if str(exo[5]) == "Pas de matérielle":
            if str(exo[1,3]) not in str(listexo):
                listexo.append(exo[1,3])


print(listexo)
