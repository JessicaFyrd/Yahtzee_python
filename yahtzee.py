import random
from abc import ABC, abstractmethod


class Joueur(ABC) : # hériter de ABC(Abstract base class)  
    def __init__(self,pseudo):
        self.pseudo = pseudo
        self.score = 0 
        self.play = 1 

    #Setter
    def setPseudo(self,pseudo):
        self.pseudo = pseudo
    
    def setScore(self,score):
        self.score = score

    #Getter
    def getPseudo(self):
        print(self.pseudo)
    
    def getScore(self):
        print(self.score)

    #Relancer les dés
    @abstractmethod  # un décorateur pour définir une méthode abstraite
    def relancerDe(self):
        pass


class JoueurHumain(Joueur) :
    #Relancer les dés (choix utilisateur)
    def relancerDe(self):
        #Demande à l'utilisateur
        choix = input('Souhaitez vous relancer les dés ? O ou N : ')
        
        #Si le choix n'est pas une entrée valide
        while (choix != 'O' and choix != 'Oui' and choix != 'Oui' and choix != 'oui' and choix != 'N' and choix != 'n' and choix != 'Non' and choix != 'non') :
            print('Vous devez choisir O ou N. ')
            choix = str(input('Souhaitez vous relancer les dés ? O ou N : '))
        
        #Mettre la variable de lancé de dé à 0 ou 1 selon la réponse de l'utilisateur
        if choix == 'O' or choix == 'o' or choix == 'Oui' or choix == 'oui':
            self.play = 1
            print("Relancer des dés :")
        elif choix == 'N' or choix == 'n' or choix == 'Non' or choix == 'non':
            self.play = 0  


class JoueurOrdi(Joueur) :
    #Relancer les dés (aléatoires)
    def relancerDe(self):
        self.play = random.randrange(0, 2, 1)
        if (self.play == 1):
            print("Relancer des dés :")


class Des :
    des = list()

    #Initialisation à 0 des 6 dés
    def __init__(self):
        for i in range (6) :
            self.des.append(0)
    
    #Lancée des 6 dès (6x valeurs aléatoires entre 1 et 6)
    def setNumDes(self):
        for i in range (6) :
            self.des[i] = random.randrange(1, 7, 1)

    #Affichage de la valeurs des 6 dès
    def getNumDes(self):
        print(self.des)
         


class PlateauDeJeu :
    n = 0
    
    def __init__(self, nbJoueur):
        #Initialisation du tour
        self.tour = 1

        #Initialisation des joueurs
        self.nbJoueur = nbJoueur
        self.listeJoueurs = list()
        self.listeJoueurs.append(JoueurHumain(f"Joueur 1"))
        for n in range(1,self.nbJoueur) :
            self.listeJoueurs.append(JoueurOrdi(f"Joueur {n + 1}"))

        #Initialisation du joueur actif
        self.indexJoueur = 0
        self.joueur = self.listeJoueurs[self.indexJoueur]

    #Passer au tour suivant
    def setTour(self,tour) :
        self.tour = tour + 1

    #Afficher le numéro de tour
    def getTour(self):
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print("Tour : ", self.tour)
        print("\n")

    #Choisir le joueur
    def setJoueur(self, indexJoueur) :
        self.indexJoueur = indexJoueur
        self.joueur = self.listeJoueurs[self.indexJoueur]
    
    #Afficher le joueur
    def getJoueur(self):
        print(self.joueur.getPseudo())
    

class Partie :
    i = 0
    j = 0
    n = 0

    #Initialisation du de la partie (nombre de tour, plateau de Jeu et dés)
    def __init__(self, nbJoueur):
        self.nbDeTour = 13
        self.PDJ = PlateauDeJeu(nbJoueur)
        self.D = Des()

    #Début de jeu + affichage
    def debut(self):
        self.state = "start"
        print("DÉBUT DE LA PARTIE\n")

    #Fin de jeu + affichage
    def finDeJeu(self):
        self.state = "stop"
        print("FIN DE LA PARTIE\n")
    
    #Trame d'une partie
    def partie(self):
        self.debut()
        for i in range (self.nbDeTour):
            self.PDJ.setTour(i)
            self.PDJ.getTour()

            for j in range (self.PDJ.nbJoueur):
                self.PDJ.setJoueur(j)
                self.PDJ.getJoueur()
                self.D.setNumDes()
                self.D.getNumDes()
                
                n = 0
                while n < 2 and self.PDJ.joueur.play == 1 :
                    self.PDJ.joueur.relancerDe()
                    if self.PDJ.joueur.play == 1 :
                        self.D.setNumDes()
                        self.D.getNumDes()
                    n = n + 1
                    
                print("\n")
                self.PDJ.joueur.play = 1

        self.finDeJeu()




jeu = Partie(2)
jeu.partie()
