# f = nom du fichier

# Version JA (non utilisée)

# def open_score_file():
#     with open("scores.txt", 'r') as filin:
#         score = filin.readlines()
#         print(score)
#         nb_line = len(score)
#         tab = nb_line * [0]
#         for i in range(len(tab)):
#             tab[i] = nb_line * [0]
#         for i in range(nb_line):
#             score[i] = score[i].rstrip('\n')
#             for j in range(nb_line):
#                 spell = score[j]
#                 spel = spell.split(";")
#                 tab[j] = spel
#     return tab
# print(open_score_file())



# Version JA (non utilisée)

# def score_comparaison1():
#     # on regarde dans le txt quel est le meilleur score on doit utiliser la fonction open_score_file afin d'utiliser
#     # le tableau avec le score
#     best_score = 0
#     with open("scores.txt", 'r') as filin:
#         score = filin.readlines()
#         nb_line = len(score)
#         tab = nb_line * [0]
#         for i in range(len(tab)):
#             tab[i] = nb_line * [0]
#         for i in range(nb_line):
#             score[i] = score[i].rstrip('\n')
#             for j in range(nb_line):
#                 spell = score[j]
#                 spel = spell.split(";")
#                 tab[j] = spel
#
#     print(tab)
#     for i in range(1, len(tab) - 1):
#         temp_score = tab[i][3]
#         temp_score2 = int(temp_score)
#         if best_score < temp_score2:
#             best_score = temp_score2
#     temp_perso_score = tab[nb_line - 1][3]
#     temp_pers = int(temp_perso_score)
#     if temp_pers > best_score:
#         best_score = temp_pers
#     return best_score
# # print(score_comparaison1())

# Versions Ethan

# Comparaison de tous les scores (non utilisée)
#     for i in range(1, len(tab) - 1):
#         temp_score = tab[i][3]
#         temp_score2 = int(temp_score)
#         if best_score < temp_score2:
#             best_score = temp_score2
#     temp_perso_score = tab[nb_ligne - 1][3]
#     temp_pers = int(temp_perso_score)
#     if temp_pers > best_score:
#         best_score = temp_pers

# # =============================================================================
# # FONCTION OUTIL : Modifier Ligne Auteur : Ethan SUISSA- en cours
# def modifierLigne(cheminAccesFichier, pId, pNom, pAngle, pScore):
#     global line
#     IdRecherche = pId + ";"
#
#     ligneAecrire = pId + ";" + pNom + ";" + pAngle + ";" + pScore
#     LigneTrouve = False
#     fichier = open(cheminAccesFichier, "a")  # ouverture du fichier à modifier
#     for line in fichier:  # boucle sur les lignes du fichier original
#         if IdRecherche in line:
#             print("modifierLigne : Id trouvé = ", pId)
#             print("Line = ", line)
#             line = ligneAecrire
#             LigneTrouve = True
#
#     if LigneTrouve == True:
#         fichier.write(line)
#     fichier.close()

