display_abs = False
display_pecs = False
display_biceps = False
ext_obliques = False
ext_obliques = False
trapèze = False
muscle_dentele = False
deltoïdes = False
Brachial = False
Biceps_Brachial = False
muscle_des_avants_bras = False
Triceps = False
Trapèze = False
Abdos = False
Fessier = False
Grand_pectoral = False
Lombaires = False
Pectoraux = False
Biceps = False
Cuisse = False
Grand_dorsal = False
mollets = False
abducteurs = False
Quadriceps = False
Ischio_jambiers = False
Triceps_Sural = False
Biceps_fémoral = False
Quadriceps_droit_de_la_cuisse = False

aucun = True # sans materiel
EnSalle = True
MaterielleAchetable = True


def get_exo():
    listexo = []
    f = open("Projet_NSI.txt", "r")
    data = f.read()
    data_sep = str(data).split('\n')

    for x in range(len(str(data).split('\n'))):
        exo = str(data_sep[x]).split(';')
        if 'Deltoïde' in str(data_sep[x]) and deltoïdes:
            if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                if str(exo[1]) not in str(listexo):
                    exm=(exo[1],exo[3])
                    listexo.append(exm)


        if 'Biceps' in str(data_sep[x]) and display_biceps:
            exo = str(data_sep[x]).split(';')
            if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                if str(exo[1]) not in str(listexo):
                    exm=(exo[1],exo[3])
                    listexo.append(exm)


        if 'Brachial' in str(data_sep[x]) and Brachial:
            exo = str(data_sep[x]).split(';')
            if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                if str(exo[1]) not in str(listexo):
                    exm=(exo[1],exo[3])
                    listexo.append(exm)


        if 'Biceps_Brachial' in str(data_sep[x]) and Biceps_Brachial:
            exo = str(data_sep[x]).split(';')
            if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                if str(exo[1]) not in str(listexo):
                    exm=(exo[1],exo[3])
                    listexo.append(exm)


        if 'muscle_des_avants_bras' in str(data_sep[x]) and muscle_des_avants_bras:
            exo = str(data_sep[x]).split(';')
            if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                if str(exo[1]) not in str(listexo):
                    exm=(exo[1],exo[3])
                    listexo.append(exm)

        if 'Triceps' in str(data_sep[x]) and Triceps:
                    if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                        if str(exo[1]) not in str(listexo):
                            exm=(exo[1],exo[3])
                            listexo.append(exm)

        if 'Trapèze' in str(data_sep[x]) and Trapèze:
                    if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                        if str(exo[1]) not in str(listexo):
                            exm=(exo[1],exo[3])
                            listexo.append(exm)


        if 'Abdos' in str(data_sep[x]) and Abdos:
                    if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                        if str(exo[1]) not in str(listexo):
                            exm=(exo[1],exo[3])
                            listexo.append(exm)

        if 'Fessier' in str(data_sep[x]) and Fessier:
                    if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                        if str(exo[1]) not in str(listexo):
                            exm=(exo[1],exo[3])
                            listexo.append(exm)

        if 'Grand pectoral' in str(data_sep[x]) and Grand_pectoral:
                    if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                        if str(exo[1]) not in str(listexo):
                            exm=(exo[1],exo[3])
                            listexo.append(exm)

        if 'Lombaires' in str(data_sep[x]) and Lombaires:
                    if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                        if str(exo[1]) not in str(listexo):
                            exm=(exo[1],exo[3])
                            listexo.append(exm)

        if 'Pectoraux' in str(data_sep[x]) and Pectoraux:
                    if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                        if str(exo[1]) not in str(listexo):
                            exm=(exo[1],exo[3])
                            listexo.append(exm)

        if 'Biceps' in str(data_sep[x]) and Biceps:
                    if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                        if str(exo[1]) not in str(listexo):
                            exm=(exo[1],exo[3])
                            listexo.append(exm)

        if 'Cuisse' in str(data_sep[x]) and Cuisse:
                    if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                        if str(exo[1]) not in str(listexo):
                            exm=(exo[1],exo[3])
                            listexo.append(exm)

        if 'Grand dorsal' in str(data_sep[x]) and Grand_dorsal:
                    if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                        if str(exo[1]) not in str(listexo):
                            exm=(exo[1],exo[3])
                            listexo.append(exm)

        if 'mollets' in str(data_sep[x]) and mollets:
                    if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                        if str(exo[1]) not in str(listexo):
                            exm=(exo[1],exo[3])
                            listexo.append(exm)

        if 'abducteurs' in str(data_sep[x]) and abducteurs:
                    if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                        if str(exo[1]) not in str(listexo):
                            exm=(exo[1],exo[3])
                            listexo.append(exm)

        if 'Quadriceps' in str(data_sep[x]) and Quadriceps:
                    if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                        if str(exo[1]) not in str(listexo):
                            exm=(exo[1],exo[3])
                            listexo.append(exm)

        if 'Ischio jambiers' in str(data_sep[x]) and Ischio_jambiers:
                    if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                        if str(exo[1]) not in str(listexo):
                            exm=(exo[1],exo[3])
                            listexo.append(exm)

        if 'Triceps Sural' in str(data_sep[x]) and Triceps_Sural:
                    if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                        if str(exo[1]) not in str(listexo):
                            exm=(exo[1],exo[3])
                            listexo.append(exm)


        if 'Biceps fémoral' in str(data_sep[x]) and Biceps_fémoral:
                    if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                        if str(exo[1]) not in str(listexo):
                            exm=(exo[1],exo[3])
                            listexo.append(exm)


        if 'Quadriceps droit de la cuisse' in str(data_sep[x]) and Quadriceps_droit_de_la_cuisse:
                    if "Pas de matériel" in str(exo[5]) and aucun or "Matérielle achetable" in str(exo[5]) and MaterielleAchetable or "A faire en salle" in str(exo[5]) and EnSalle:
                        if str(exo[1]) not in str(listexo):
                            exm=(exo[1],exo[3])
                            listexo.append(exm)


    return listexo



print(get_exo())
