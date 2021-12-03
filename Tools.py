## ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : pour le 24 mai 2021
# Fichier outils, comporte les fonctions d'écriture de la base de donnée.
# ======================================================

# ===================================================================================
# FONCTION OUTIL: Renvoie la ligne choisie du fichier indiqué dans une chaine de caractère (équivalent de read_file_line
# avec le chemin d'accès en entrée) Auteur : Ethan SUISSA - Terminé
# Sortie : Chaine de caractère qui contient la ligne récupérée
# -----------------------------------------------------------------------------------
def lireLaLignechoisie(chemin_acces, noLine):  # Entrée :  Chemin_acces = chemin d'acces du fichier, # noline = Numero
    # de la ligne
    line = ""
    # Vérifie si le chemin existe ou non
    import os.path
    if os.path.isfile(chemin_acces):
        print("Chemin ", chemin_acces, " existe")  # pour controle
        # Recupere le contenu de la ligne dans le fichier
        file = open(chemin_acces, 'r')
        for i in range(noLine):
            line = file.readline()
        file.close()
    else:
        print("Chemin ", chemin_acces, " n'existe pas")  # pour controle
    return line


# =============================================================================
# =============================================================================
# FONCTIONS OUTILS : Ecriture dans la base de donnée. Auteur : Jean-Alexis TADDEI- Terminé

# Ajout de l'id et du nom dans la base de donnée
def ajout_nom_F01(name):
    with open("scores.txt", 'r') as file:  # fonction with qui ouvre et ferme le fichier une fois la fonction terminée
        score = file.readlines()  # on met dans un tableau chaque ligne du ficher
        nb_line = len(score)  # On associe la taille du tableau à une variable pour connaître le nombre de lignes
        f = open("scores.txt", 'a')  # on réouvre le fichier en mode Ecriture
        f.write('\n')  # On revient à la ligne pour écrire dans le fichier
        nb_line = nb_line - 1  # On retire 1 aux nombres de lignes pour avoir l'id du joueur qui croissent
        id = str(nb_line)  # On doit convertir en charactère afin de pouvoir écrire dans le fichier
        f.write(
            id + ';' + name + ";")  # On écrit dans le fichier l'id ainsi que le nom récupérer en variable de la fonction
        # Possibilité de faire plusieurs "file.write"  à la suite ou concaténer les chaines
        return id


# Ajout de l'angle dans la base de donnée.
def ajout_angle_F02(angle):
    with open("scores.txt",
              "a") as file:  # On ouvre le ficher en mode écriture avec la fonction with qui va fermer le fichier une fois la fonction terminée
        ang = str(
            angle)  # L'angle récupérer en variable de la fonction doit etre converti en charatère afin de pouvoir l'écrire dans le fichier
        file.write(ang + ";")  # On écrit l'angle dans le fichier à la suite des autres données du joueur


# Ajout du score dans la base de donnée.
def ajout_score_F0(score):  # fenetre de jeu
    with open("scores.txt",
              "a") as f:  # On ouvre le ficher en mode écriture avec la fonction with qui va fermer le fichier une fois la fonction terminée
        sco = str(
            score)  # On converti la variable récupérer qui est un nombre qu'on va convertir en charactère pour pouvoir l'écrire dans le ficher
        f.write(sco)  # On écrit le score dans le fichier à la suite des autres données du joueur


# =============================================================================
# FONCTION OUTIL : Lecture de la base de donnée. Auteur : Jean-Alexis TADDEI- Terminée


def open_score_file2():
    with open("scores.txt",
              'r') as filin:  # On ouvre le ficher avec la fonction with qui va fermer le fichier une fois la fonction terminée
        score = filin.readlines()  # on attribue chaque ligne du ficher dans un tableau
        nb_line = len(score)  # On compte le nombre de ligne que possède le fichier
        tab = []  # On déclare un nouveau tableau
        for i in range(nb_line):  # On ouvre une boucle
            score[i] = score[i].rstrip(
                '\n')  # Par soucis d'affichage on doit enlever les \n qui étaient considérés comme un retour à la ligne
            # dans un txt mais pas dans un tableau
            spell = score[i]  # On associe à une variable la ligne de associée à la boucle
            spel = spell.split(
                ";")  # On enlève les ';' de la ligne afin de récupérer un tableau avec de la forme [id, name, angle, score]
            tab.append(spel)  # On ajoute a un nouveau tableau chaque tableau créé dans la boucle
        filin.close()  # On ferme finalement le fichier
    return tab, nb_line  # On retourne le tableau avec toutes les données et le nombre de ligne qui va nous servir


# =============================================================================
# FONCTION OUTIL : Comparaison Score. Auteur : Jean-Alexis TADDEI- Terminée


def score_comparaison(Score, IdJoueur):
    # on regarde dans le txt quel est le meilleur score on doit utiliser la fonction open_score_file afin d'utiliser
    # le tableau avec le score
    tab, nb_ligne = open_score_file2()  # On récupère les 2 variables retournées avec la fonction open_score_file2
    Old_best_score = int(tab[IdJoueur + 1][3])
    best_score = int(tab[IdJoueur + 1][3])  # tab est un tableau en 2 dimensions, on prend le meilleur score à la ligne
    # du joueur (4e colonne, ligne de l'identifiant + 2, avec un décalage de -1 pour les indices du tableau).
    if Score >= best_score:  # on compare le score avec le meilleur score du joueur, s'il est supérieur, la variable
        # meilleur score prend celle du score de la partie.
        best_score = Score
    return best_score, Old_best_score
    # Test : Score = 1
    # print(score_comparaison2(Score))


# =============================================================================
# FONCTION OUTIL : Modifie précisément un élément de la ligne de la base de donnée. Auteur : Ethan SUISSA- terminé

import fileinput

def ModifPrecisFichier(NumLigne, NumElt, Modif):
    tab, nbLignes = open_score_file2()  # Lecture de la base de donnée
    # Enregistrement de la ligne à modifier
    OldLigne = lireLaLignechoisie("scores.txt", NumLigne)
    OldLigne = OldLigne.rstrip('\n')  # Suppression du '\n' de l'ancienne ligne
    print("Ancienne ligne", OldLigne)  # Pour contrôle
    # Enregistrement de la ligne à appliquer à la place d'OldLine
    tab[NumLigne - 1][NumElt] = str(Modif)  # Modification de l'élément demandé
    NewLigne = ""
    for i in range(3):
        NewLigne += tab[NumLigne - 1][i] + ";"  # Même addition que précedemment
    NewLigne += tab[NumLigne - 1][3]  # Ligne à appliquer à la place de l'ancienne
    print("Nouvelle ligne", NewLigne)
    with fileinput.input("scores.txt", inplace=True) as f:  # Configure le fichier pour cette modification (trouvé sur
        # internet).
        for line in f:
            new_line = line.replace(OldLigne, NewLigne)  # Modification de la ligne en remplacant l'ancienne par
            # la nouvelle.
            print(new_line, end='')  # n'affiche rien mais enlève les blancs intermédiaires
    # Test : ModifPrecisFichier(3, 2, 1)
