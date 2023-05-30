import random


class Joueur :
    def __init__(self,pseudo):
        self.pseudo = pseudo
        self.score = 0 
        self.play = 1 
    
    def getPseudo(self):
        print(self.pseudo)

    def getScore(self):
        print(self.score)


class Des :
    des = list()

    def __init__(self):
        for i in range (6) :
            self.des.append(0)
    
    def setNum(self):
        for i in range (6) :
            self.des[i] = random.randrange(1, 7, 1)

    def getNum(self):
        print(self.des)
         


class PlateauDeJeu :
    n = 0
    
    def __init__(self, nbJoueur):
        #Initialisation du tour
        self.tour = 1

        #Initialisation des joueurs
        self.nbJoueur = nbJoueur
        self.listeJoueurs = list()
        for n in range(self.nbJoueur) :
            self.listeJoueurs.append(Joueur(f"Joueur {n + 1}"))

        #Initialisation du joueur actif
        self.indexJoueur = 0
        self.joueur = self.listeJoueurs[self.indexJoueur]

    def setTour(self,tour) :
        self.tour = tour + 1

    def getTour(self):
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print("Tour : ", self.tour)
        print("\n")

    def setJoueur(self, indexJoueur) :
        self.indexJoueur = indexJoueur
        self.joueur = self.listeJoueurs[self.indexJoueur]
    
    def getJoueur(self):
        print(self.joueur.getPseudo())
    
    def relancerDe(self):
        self.play = random.randrange(0, 2, 1)
        if (self.play == 1):
            print("Relancer des dés :")
    

class Partie :
    i = 0
    j = 0
    n = 0

    def __init__(self, nbJoueur):
        self.nbDeTour = 13
        self.PDJ = PlateauDeJeu(nbJoueur)
        self.D = Des()

    def debut(self):
        self.state = "start"
        print("DÉBUT DE LA PARTIE\n")

    def finDeJeu(self):
        self.state = "stop"
        print("FIN DE LA PARTIE\n")
    
    def partie(self):
        self.debut()
        for i in range (self.nbDeTour):
            self.PDJ.setTour(i)
            self.PDJ.getTour()
            for j in range (self.PDJ.nbJoueur):
                self.PDJ.setJoueur(j)
                self.PDJ.getJoueur()
                self.D.setNum()
                self.D.getNum()
                for n in range (2):
                    self.PDJ.relancerDe()
                    if self.PDJ.play == 1 :
                        self.D.setNum()
                        self.D.getNum()
                    
                print("\n")
        self.finDeJeu()




jeu = Partie(2)
jeu.partie()
