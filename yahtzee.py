import random


class Joueur :
    def __init__(self,pseudo):
        self.pseudo = pseudo
        self.score = 0  
    
    def getPseudo(self):
        print(self.pseudo)

    def getScore(self):
        print(self.score)


class PlateauDeJeu :
    n = 0
    
    def __init__(self, nbJoueur):
        #Initialisation du tour
        self.tour = 1

        #Initialisation des joueurs
        self.nbJoueur = nbJoueur
        self.listeJoueurs = []
        for n in (self.nbJoueur) :
            self.listeJoueurs[n] = Joueur("Joueur ",n + 1)

        #Initialisation du joueur actif
        self.indexJoueur = 0
        self.joueur = self.listeJoueurs[self.indexJoueur]

    def setTour(self,tour) :
        self.tour = tour + 1

    def getTour(self):
        print("Tour : ", self.tour)

    def setJoueur(self, indexJoueur) :
        self.indexJoueur = indexJoueur
        self.joueur = self.listeJoueurs[self.indexJoueur]
    
    def getJoueur(self):
        print(self.joueur.getPseudo())
    

class Partie :
    i = 0
    j = 0

    def __init__(self, nbJoueur):
        self.nbDeTour = 13
        self.PDJ = PlateauDeJeu(nbJoueur)

    def debut(self):
        self.state = "start"
        print("Début de la partie \n")

    def finDeJeu(self):
        self.state = "stop"
        print("Fin de la partie \n")
    
    def partie(self):
        self.debut()
        for i in range (self.nbDeTour):
            self.PDJ.setTour(i)
            self.PDJ.getTour()
            for j in range (self.PDJ.nbJoueur):
                self.PDJ.setJoueur(j)
                self.PDJ.getJoueur()
            print("\n")
        self.finDeJeu()




jeu = Partie(2)
jeu.partie()
