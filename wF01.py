# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : pour le 24 mai 2021
# Fichier F01 = "ECRAN D'ACCUEIL"

# ======================================================

# =====================
# Bibliothèques et importations :

from wF03 import *
from tkinter import *  # '*' signifie qu'on importe toutes les modifications d'un fichier
from Tools import *
from wF02 import F02
from PIL import Image
from PIL.ImageTk import PhotoImage


# ====================
# Programme :
class F01(Tk):  # declaration de l'objet F01

    # *****************************************
    # Constructeur de l'objet F01 : ne pas supprimer, sert pour mettre les paramètres et fonctions propres à l'objet.
    def __init__(self, IDJoueur):
        Tk.__init__(self)
        print("*** F01 ***")  # Pour controle en console
        self.title("F01")  # Le titre de la fenêtre
        self.minsize(1200, 700)  # Initialisation de la taille de fenêtre

        self.IdJoueur = IDJoueur  # L'ID représente l'identifiant de chaque joueur, c'est le premier élément de chaque
        # ligne de la base de donnée (fichier scores.txt). Il passe dans toutes les fenêtres pour confirmer que c'est
        # toujours le même joueur qui joue au jeu (identité du joueur définie par le nom et l'appui de "Valider"), cela
        # permet aux fonctions qui modifient la base de données de modifier la ligne du joueur actif uniquement. Il sert
        # aussi pour déverouiller les commandes d'Entrée d'Angle et de lancer du jeu, ce déverouillage s'exécute une
        # fois pour chaque joueur (pas besoin de réecrire le nom à chaque fois pour cela). Cette transmission est
        # nécessaire pour que le jeu ne soit pas affectée par la perte de données crée par les "self.destroy".

        # Une méthode séparée pour construire le contenu de la fenêtre
        self.Largeur = 1500  # Paramètre représentant la largeur de la zone du Canevas
        self.Hauteur = 1000  # Hauteur de la zone du Canevas.

        self.paddingtop = 100  # leftPadding et Paddingtop sont des variables de placement pour les boutons, ce qui
        # permet de définir des unités de mesure dans le placement.
        self.leftPadding = 40

        # Paramètres plein écran
        self.fullScreenState = True
        self.attributes("-fullscreen", self.fullScreenState)
        self.bind("<F11>", self.toggleFullScreen)
        self.bind("<Escape>", self.quitFullScreen)
        self.createWidgets()  # Une méthode séparée pour construire le contenu de la fenêtre

    # **************************************
    # Fonction/Méthode de création des widgets.
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement

        # ==================================================
        # FONCTIONS WIDGET ::::::::

        # Affichage du fond d'écran de F01
        # ELEMENT GRAPHIQUE : <Image en FOND> = [Libellé I02]: fond de F01
        self.Photofond = Image.open(os.getcwd() + "/IMAGES/ImageF01/nebuleuse.jpg")
        self.Photofond = self.Photofond.resize((self.Largeur, self.Hauteur), Image.ANTIALIAS)
        self.FondF01 = PhotoImage(self.Photofond)
        self.CanvasMenu = Canvas(self, width=self.Largeur, height=self.Hauteur)
        self.ImgFondF01 = self.CanvasMenu.create_image(self.Largeur // 2, self.Hauteur // 2, image=self.FondF01)
        self.CanvasMenu.pack(padx=5, pady=5)  # .pack sert à placer le texte
        self.CanvasMenu.tag_lower(self.ImgFondF01)  # Canevas.tag_lower(objet) sert à faire passer un objet du Canevas à

        # l'arrière plan, àl'inverse de tag_raise qui le met au premier.

        # =================
        # FONCTION Récupération Nom et enregistrement dans score.txt, met à jour l'ID de joueur et permet le premier
        # déverouillage des commandes "jouer" et "Configuration Angle"
        def RecupNameDever():
            "Enregistrer le ,nom"
            Name = EntreeNom.get()
            print("Nom :", Name)
            msg = "En Avant " + Name + "!"
            if Name != "":  # Si la fenêtre d'entrée du nom n'est pas vide :
                # On vérifie si le joueur existe dans la base de donnée
                tab, NbLignes = open_score_file2()
                JoueurExist = False
                for i in range(NbLignes):
                    if tab[i][1] == Name:
                        JoueurExist = True
                        self.IdJoueur = i - 1  # L'id du joueur est toujours égal à la valeur du numéro de ligne - 2
                        # mais on rajoute 1 pour le décalage du tableau
                        break
                # Si le joueur n'existe pas, on initialise son profil
                if not JoueurExist:
                    # Ajout du nom dans la base
                    ajout_nom_F01(Name)  # A configurer pour pas à faire à chaque fois
                    ajout_angle_F02(0)
                    ajout_score_F0(0)  # Angle et meilleur score sont à 0 car nouveau profil
                    self.IdJoueur = NbLignes - 1  # -1 l'ID est à la ligne NbLignes-1, on ajoute aussi le décalage
                    # de -2.
                    # Déverouillage des boutons
                self.DeverouilCommands()
                self.MajListe()  # Permet la mise à jour instantannée de la listbox.
            else:
                msg = "Pas de nom, pas de jeu !"
            self.messageUtilisateurNom.set(msg)  # Pour mise à jour texte écran

        # ==================================================
        # ELEMENTS GRAPHIQUES::::::::

        # ...........< L A B E L S > .........................

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T06] : intervalle angles possibles
        lblEntreAngle = Label(self, bg="purple", fg="white",
                              text="Angle entre 0 et 360° :")  # Nom de la fenêtre en rouge à déclarer comme au
        # dessus (avec le nom de fenêtre qu'on veut)
        lblEntreAngle.place(x=self.leftPadding, y=self.paddingtop + 220)

        # Création d'un widget Label (texte 'Nom'),ELEMENT GRAPHIQUE : <Label> = [Libellé T01]: Titre jeu
        Label1 = Label(self, text="Un Heros contre Galacticov ", font=('Arial', 20), fg='blue')
        # Label1.pack(padx=1, pady=1)
        Label1.place(x=self.leftPadding, y=50)

        # Création d'un widget Label (texte 'Nom'),ELEMENT GRAPHIQUE : <Label> = [Libellé T05]: demande de saisie du pseudo
        Label1 = Label(self, text='Quel est ton nom ?', bg="purple", fg="white",
                       font=("Arial", 20))  # ajouter: "jeune protecteur de la Galaxie?"
        # Label1.pack(padx=1, pady=1)
        Label1.place(x=self.leftPadding, y=self.paddingtop + 50)

        # ...........< E N T R Y ' S > .......................

        # ELEMENT GRAPHIQUE : <Entry> = [Libellé E01] : Entrée du pseudo
        # Création d'un widget Entry (champ de saisie)
        Nom = StringVar()  # ELEMENT GRAPHIQUE : <Label> = [Libellé SV01] :message apres saisie nom
        EntreeNom = Entry(self, textvariable=Nom, bg='bisque', fg='RoyalBlue1', font=("Arial", 20))
        # bg = couleur du fond d'écran du texte entré, fg = couleur du texte entré, font = police et taille du texte.
        EntreeNom.focus_set()  # Inutile de cliquer pour entrer le nom.
        EntreeNom.place(x=self.leftPadding + 300, y=self.paddingtop + 50)

        # ...........< L A B E L S  V A R I A B L E S > .........................

        # ELEMENT GRAPHIQUE : <Label> = [StringVar Sv02] : Message vérifiant le nom
        # Le stringvar est un label de textes qu'on peut faire varier au cour du programme avec le .set().
        self.messageUtilisateurNom = StringVar()  # Variable de message d'erreur de saisie type stringvar() pour
        self.messageUtilisateurNom.set("...")  # maj Label pertinent.
        # Declaration et Placement du label avec le message du nom.
        self.LblMessage = Label(self, textvariable=self.messageUtilisateurNom, bg="MediumOrchid4", fg="white",
                                font=("Arial", 15))  # Changement du "texte" en "texteVariable" pour le StringVar.
        self.LblMessage.place(x=self.leftPadding + 300, y=self.paddingtop + 150)

        # ELEMENT GRAPHIQUE : <Label> = [StringVar Sv03] :Message vérifiant l'angle
        # Message après vérifiaction de l'entrée de l'angle
        self.messageUtilisateurAngle = StringVar()  # Variable de message d'erreur de saisie type stringvar() pour
        self.messageUtilisateurAngle.set("...")  # maj Label pertinent.

        # Declaration et Placement du label avec le message de l'angle.
        self.LblMessage = Label(self, textvariable=self.messageUtilisateurAngle, bg="MediumOrchid4", fg="white")
        self.LblMessage.place(x=self.leftPadding + 300, y=self.paddingtop + 220)

        # ...........< B U T T O N S >........................
        # Boutons "configuration commande" et "valider" en haut

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B02] : enregistrement du pseudo
        self.BoutonValidNom = Button(self, text="Valider", bg="RoyalBlue1", fg="white", font=("Arial", 15),
                                     command=RecupNameDever)

        self.BoutonValidNom.place(x=self.leftPadding, y=self.paddingtop + 150)

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B03] : Ouverture de F03, fenêtre d'information.
        BoutConfCom = Button(self, text="Informations Jeu", bg="RoyalBlue1", fg="white", font=("Arial", 15), command=self.commandeOuvreF03)
        BoutConfCom.place(x=self.leftPadding + 400, y=self.paddingtop + 600)

        print("ID =", self.IdJoueur)  # Pour control.
        if self.IdJoueur != 0:  # Si le joueur est définie après l'entrée du nom (le placement ici sert si on réouvre
            # F01 pour ne pas devoir ré-entrer le nom).
            # Déverouillage des boutons
            self.DeverouilCommands()

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B06] : bouton pour quitter l'application
        self.quitButton = Button(self, bg="Royalblue3", fg="white", font=("Arial", 15), text="Quitter", command=self.destroy)
        self.quitButton.place(x=self.leftPadding + 300, y=self.paddingtop + 600)


        # ...........< L I S T B O X ' S > .......................
        # ELEMENT GRAPHIQUE : <Label> = [Libellé L01] : Liste des ID des joueurs de la base de données
        # (déclaration & position), une listbox permet leur affichage.
        self.AffID = Listbox(self)
        self.AffID.place(x=self.leftPadding + 800, y=50, width=100, height=500)

        # ELEMENT GRAPHIQUE : <Label> = [Libellé L02] : Liste des noms des joueurs de la base de données
        # (déclaration & position)
        self.AffNom = Listbox(self)
        self.AffNom.place(x=self.leftPadding + 900, y=50, width=100, height=500)

        # ELEMENT GRAPHIQUE : <Label> = [Libellé L03] : Liste des Angles des joueurs de la base de données
        # (déclaration & position)
        self.AffAngle = Listbox(self)
        self.AffAngle.place(x=self.leftPadding + 1000, y=50, width=100, height=500)

        # ELEMENT GRAPHIQUE : <Label> = [Libellé L04] : Liste des score des joueurs de la base de données
        # (déclaration & position)
        self.AffScore = Listbox(self)
        self.AffScore.place(x=self.leftPadding + 1100, y=50, width=100, height=500)

        # Alimentation des listboxs
        self.MajListe()

    # **************************************
    # FONCTIONS DE L'OBJET::::::::

    # ======================
    # FONCTION OUTIL pour déverouiller les commandes si joueur enregistré (id != 0 ou nom entré)
    def DeverouilCommands(self):
        # ELEMENT GRAPHIQUE : <Button> = [Bouton B05] :bouton pour lancer le jeu et ouvrir F02
<<<<<<< HEAD
        self.ouvreF02 = Button(self, text="jouer", bg="Royalblue3", fg="white", font=("Arial", 15)", command=self.commandeOuvreF02)
=======
        self.ouvreF02 = Button(self, bg="Royalblue3", fg="white", font=("Arial", 15), text="jouer", command=self.commandeOuvreF02)
>>>>>>> c75964bad89abec77f817725d7249e763808de6b
        self.ouvreF02.place(x=self.leftPadding, y=self.paddingtop + 600)


        # ELEMENT GRAPHIQUE : <Entry> = [E02]: pour saisir l'angle
        self.entreAngle = Entry(self,bg="Royalblue3", fg="white", font=("Arial", 18))
        self.entreAngle.place(x=self.leftPadding, y=self.paddingtop + 250, width=100)

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B04] : "Appliquer (Enregistrer) l'angle"
<<<<<<< HEAD
        self.AppliqAngle = Button(self, text="Appliquer l'angle", bg="Royalblue3", fg="white", font=("Arial", 15), command=self.EnregistrAngle)
=======
        self.AppliqAngle = Button(self, bg="Royalblue3", fg="white", font=("Arial", 15), text="Appliquer l'angle", command=self.EnregistrAngle)
>>>>>>> c75964bad89abec77f817725d7249e763808de6b
        self.AppliqAngle.place(x=self.leftPadding + 300, y=self.paddingtop + 250)


        # =====================
        # FONCTION Récupération Angle et enregistrement dans score.txt pour application

    def EnregistrAngle(self):  # Fonction doit être mise avant sinon erreur
        TextAngleEnDegree = self.entreAngle.get()
        # Etape 1 : Ajustement de l'angle pour un résultat convenable.
        AngleEnDegree, message = self.TrtAngle(TextAngleEnDegree)
        print("Angle en degree = ", AngleEnDegree)  # Pour controle

        # Etape 2 : Envoi de l'angle dans score.txt
        if message == "Angle enregistré":
            ModifPrecisFichier(self.IdJoueur + 2, 2,
                               AngleEnDegree)  # Explication de l'appel : voir l'appel identique dans F02
            self.MajListe()  # Pour mise à jour instantannée des listbox

        # ========================
        # FONCTION OUTIL Traite l'angle pour le rendre enregistrable et utilisable.

    def TrtAngle(self, TextAngleEnDegree):
        # Récupération angle de la zone de Saisie ou pose de 0
        AngleEnDegree = 0
        if TextAngleEnDegree != "":
            try:  # Essai la tranformation en int en vérifiant les erreurs avant (pour éviter un plantage total).
                AngleEnDegree = int(TextAngleEnDegree)
                if AngleEnDegree >= 360 or AngleEnDegree <= -360:
                    AngleEnDegree = AngleEnDegree % 360  # Création d'un modulo pour ajuster les angles trop grand.
                if AngleEnDegree < 0:
                    AngleEnDegree += 360  # Angle ne change pas mais on le replace sur l'intervalle [0; 360]
                msg = "Angle enregistré"  # ELEMENT GRAPHIQUE : <Label> = [Libellé SV02] : si angle bon
            except ValueError:
                msg = ">> Angle doit etre un entier "  # ELEMENT GRAPHIQUE : <Label> = [Libellé SV02] : si angle mauvais
                print(msg)  # Pour contrôle en console
        else:
            msg = "Pas d'angle enregistré"  # ELEMENT GRAPHIQUE : <Label> = [Libellé SV02] : si pas d'angle
        self.messageUtilisateurAngle.set(msg)  # Pour mise à jour texte écran
        print(str(self.messageUtilisateurAngle.get()))  # Pour Controle
        # AffAngle.insert(END, AngleEnDegree)
        return AngleEnDegree, msg

    # ========================
    # FONCTIONS OUTILS réglant le plein écran (déjà expliquées).
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)

    # ========================
    # FONCTION réglant la mise à jour des listbox.
    def MajListe(self):
        # Initialisation des listboxs par suppression de leur contenu précédent.
        self.AffID.delete(0, END)
        self.AffNom.delete(0, END)
        self.AffAngle.delete(0, END)
        self.AffScore.delete(0, END)

        # Remplissage
        tab, nb_ligne = open_score_file2()  # Lecture du ficher score.txt
        for i in range(0, nb_ligne):
            self.AffID.insert(END, tab[i][0])  # Remplissage de la listbox des ID par tous les éléments de la première
            # colonne du tableau contenant la base de donné, ce sont donc bien les ID.
        for i in range(0, nb_ligne):
            self.AffNom.insert(END, tab[i][1])  # Même principe avec la colonne 2 pour la liste des noms.
        for i in range(0, nb_ligne):
            self.AffAngle.insert(END, tab[i][2])  # Même principe avec la colonne 3 pour la liste des angles.
        for i in range(0, nb_ligne):
            self.AffScore.insert(END, tab[i][3])  # Même principe avec la colonne 4 pour la liste des scores.

    # COMMANDE : ouvre F02 (Jouer)
    def commandeOuvreF02(self):
        self.destroy()  # ferme F01
        # ouvre F02
        app = F02(self.IdJoueur)  # implémente l'objet app
        app.focus_force()  # Force le focus sur la fenetre
        app.mainloop()

    def commandeOuvreF03(self):
        self.destroy()  # ferme F01
        # ouvre F02
        app = F03(self.IdJoueur)  # implémente l'objet app
        app.focus_force()  # Force le focus sur la fenetre
        app.mainloop()
