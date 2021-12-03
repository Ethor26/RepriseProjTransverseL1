# PersoPion.move(img_Vaisseau,self.PosX,self.PosY)
#
#
# img_Vaisseau = PhotoImage(file="IMAGES/faucon millenium-3.png")
#         CanevasJeu.create_image(self.PosX, self.PosY, anchor=NW, image=img_Vaisseau)
#         img_Vaisseau.zoom(1,1)
#
# # on passe le voleur au premier plan
# self.CanevasJeu.tag_raise(img_Vaisseau, ALL)

# Inutilisés : programmation collisions
# i['dx'] = -i['dx']
# CopieObjBall = self.balls[j]
# CopieCoordBall = self.balles[j]
# Modif de balls, balles et des coordonnées de départ à faire
# self.CanevasJeu.delete(self.balls[j])

# di['dy'] = -i['dy']
# Collision entre les balles
# ordre = 1/2, 1/3, 1/4, 2/3, 2/4, 3/4
#         for i in range(len(self.balles)):
#             j = i + 1
#             while j < len(self.balles):
#                 # Test si (ray1+ray2)² > dist(x1-x2)² + dist(y1-y2)²
#                 # et interverti les dx et dy
#                 if (self.balles[i]['ray'] + self.balles[j]['ray']) ** 2 > \
#                         ((self.balles[i]['x'] - self.balles[j]['x']) ** 2 +  # \
#                          (self.balles[i]['y'] - self.balles[j]['y']) ** 2):
#                     self.balles[i]['dx'], self.balles[j]['dx'] = self.balles[j]['dx'], self.balles[i]['dx']
#                     self.balles[i]['dy'], self.balles[j]['dy'] = self.balles[j]['dy'], self.balles[i]['dy']
#                  j += 1

# Autre methode pour modifier un texte sans stringVar:
# self.compteur_lbl.configure(text=str(int(self.CompteurScore)))
# self.compteur_lbl['text'] = str(int(self.CompteurScore))

# Creation et deplacement d'ovale (inutilisé : remplacé par image)

# # Objet associé à CoordObstaclesGauche
        #         ObjObstacleGauche = self.CanevasJeu.create_oval(CoordObstacleGauche['x'] - CoordObstacleGauche['ray'],
        #                                                         CoordObstacleGauche['y'] - CoordObstacleGauche['ray'],
        #                                                         CoordObstacleGauche['x'] + CoordObstacleGauche['ray'],
        #                                                         CoordObstacleGauche['y'] + CoordObstacleGauche['ray'],
        #                                                         fill='yellow') # Couleur = jaune.
        #         # Objet associé à CoordObstaclesHaut
        #         ObjObstacleHaut = self.CanevasJeu.create_oval(CoordObstacleHaut['x'] - CoordObstacleHaut['ray'],
        #                                                       CoordObstacleHaut['y'] - CoordObstacleHaut['ray'],
        #                                                       CoordObstacleHaut['x'] + CoordObstacleHaut['ray'],
        #                                                       CoordObstacleHaut['y'] + CoordObstacleHaut['ray'],
        #                                                       fill='yellow')
        #         # Objet associé à CoordObstaclesDroite
        #         ObjObstacleDroite = self.CanevasJeu.create_oval(CoordObstacleDroite['x'] - CoordObstacleDroite['ray'],
        #                                                         CoordObstacleDroite['y'] - CoordObstacleDroite['ray'],
        #                                                         CoordObstacleDroite['x'] + CoordObstacleDroite['ray'],
        #                                                         CoordObstacleDroite['y'] + CoordObstacleDroite['ray'],
        #                                                         fill='yellow')
        #         # Objet associé à CoordObstaclesBas
        #         ObjetObstacleBas = self.CanevasJeu.create_oval(CoordObstacleBas['x'] - CoordObstacleBas['ray'],
        #                                                        CoordObstacleBas['y'] - CoordObstacleBas['ray'],
        #                                                        CoordObstacleBas['x'] + CoordObstacleBas['ray'],
        #                                                        CoordObstacleBas['y'] + CoordObstacleBas['ray'],
        #                                                        fill='yellow')
        #         # La liste "balls" prend l'ensemble des objets obstacles, elle sera lue par les
        #         # fonction de déplacement.
        #         self.balls = [ObjObstacleDroite, ObjObstacleHaut, ObjObstacleGauche, ObjetObstacleBas]

# # ObjetObstacleRandom = self.CanevasJeu.create_oval(CoordObstacleRandom['x'] - CoordObstacleRandom['ray'],
#             #                                                               CoordObstacleRandom['y'] - CoordObstacleRandom['ray'],
#             #                                                               CoordObstacleRandom['x'] + CoordObstacleRandom['ray'],
#             #                                                               CoordObstacleRandom['y'] + CoordObstacleRandom['ray'],
#             #                                                               fill='yellow')

# La fonction .coord est ici utilisée pour
                # redessiner un ovale avec 4 paramètre (et non pas un rectangle comme avec le personnage).
                # self.CanevasJeu.coords(self.balls[i],
        #                                        self.balles[i]['x'] - self.balles[i]['ray'],
        #                                        self.balles[i]['y'] - self.balles[i]['ray'],
        #                                        self.balles[i]['x'] + self.balles[i]['ray'],
        #                                        self.balles[i]['y'] + self.balles[i]['ray'])

# # Fonction test, non utilisé pour Bdd
# def ajout_score(f, id, user, angle, score):
#     with open(f, 'a') as file:
#         file.write('\n')
#         file.write(id)
#         file.write(';')
#         file.write(user)
#         file.write(';')
#         file.write(angle)
#         file.write(';')
#         file.write(score)

# ========================================================================================
# FONCTION OUTIL: fonction COMPLEMENTAIRE aux précédentes qui retourner la clé d'un dictionnaire avec en entrée
# celui-ci et une de ses valeurs.  Auteur : Ethan SUISSA - Terminé
# def find_key(Dict, Val):
#     for key, val in Dict.items():
#         if Val == val:
#             return key