import random,pygame, sys
from math import *
from Animaux import *
from tkinter import *
from tkinter import messagebox

class Biocenose:
    ''' Genere les listes des animaux et leurs interactions '''

    def __init__(self):
        self.l_loup = []
        self.l_loutre = []
        self.l_poisson = []
    
    #---------------------------------------------------------------
    # Fonctions diverses pour simplifier le code

    # cette méthode affiche la liste dans le terminal
    def affichage(self,liste):
        for i in range(len(liste)):
            print(liste[i].__str__())
    
    def id(self,liste):
        '''Attribuer les identifiants'''
        for i in range(len(liste)):
            liste[i].id = i
    
    def ajouter(self, liste, nombre):
        ''' Ajoute les nouveaux animaux'''
        
        for i in range(nombre):
            
            if (liste == self.l_poisson):
                liste.append(Poisson(0))
                
            if (liste == self.l_loutre):
                liste.append(Loutre(0))
                
            elif (liste == self.l_loup):
                liste.append(Loup(0))

        self.id(liste)
        
    def morts_des_animaux(self, liste, nombre):

        for i in range(nombre):
 
                liste.remove(random.choice(list(liste)))

    def viabilite(self, liste) :
        if (len(liste) <= 1 or len(liste) >= 10000 ):
            return True
                
    #---------------------------------------------------------------
    # Listes d'initialisation

    def liste_des_animaux (self, liste, nombre):
        ''' Cette fonction répertorie les animaux dans des listes appropriés à leur race'''
        liste = []

        for i in range(nombre):
            
            if liste == self.l_poisson:
                liste.append(Poisson(-1))
                self.l_poisson.append(liste[i])

            elif liste == self.l_loutre:
                liste.append(Loutre (-1))
                self.l_loutre.append(liste[i])

            elif liste == self.l_loup:
                liste.append(Loup(-1))
                self.l_loup.append(liste[i])

            self.id(liste)
    
    #---------------------------------------------------------------
    # Reproduction des Animaux dans notre ecosysteme

    def compter_femelle(self, liste):
        
        femelle_fertile = 0
        male = 0

        # Compter le nombre de male et de femelle fertile
        for i in range(len(liste)):

            if liste[i].sexe == 0 and liste[i].age >= 2 :            
                femelle_fertile = femelle_fertile + 1

            elif liste[i].sexe == 1 :
                male = male + 1

        # Avoir le même nombre de male et de femelle
        if femelle_fertile > male :
            femelle_fertile = male

        return(femelle_fertile)

    def reproduction(self, liste):
        '''Fonction de reproduction des animaux'''

        femelle_fertile = self.compter_femelle(liste)

        # Nombre de femelle pleine
        Pourcentage_FP = float(femelle_fertile) * (random.uniform(0.5,1.0))
        self.nb_femelle_pleine = ceil(Pourcentage_FP)

        # Reproductions des Loutres et poissons
        self.nb_bebe = 0
        alea = 0

        if liste == self.l_poisson or liste == self.l_loutre:

            for i in range(self.nb_femelle_pleine):

                if (liste == self.l_poisson):
                    alea = random.randint(3,10)
                
                elif (liste == self.l_loutre):
                    alea = random.randint(4,6)
            
                self.nb_bebe = self.nb_bebe + alea

            self.ajouter(liste, self.nb_bebe)
        
        # Reproduction des Loups

        if liste == self.l_loup and femelle_fertile > 0:
            self.nb_bebe = random.randint(2,4)

            self.ajouter(liste, self.nb_bebe)

        return self.nb_bebe
    #---------------------------------------------------------------
    # Consommation des animaux dans notre ecosysteme

    def consommation(self, listepredateur, listeproie):

        self.nbproies = 0
        self.morts = 0

        # taux de consomation
        x = int(floor(len(listeproie)/len(listepredateur)))
        
        # enclenchement de famine si x < à la valeur maximale de consommation
        def famine():

            self.morts = int(ceil(len(listepredateur)*0.3))

            self.morts_des_animaux(listepredateur, self.morts)

        # consommation des proies
        for i in range(len(listepredateur)): 

            # loup
            if (listepredateur == self.l_loup):
                        
                if (x > 2):
                    self.nbproies = self.nbproies + random.randint (1,2)
                
                else :
                    self.nbproies = self.nbproies + random.randint(0,1)
                    
            # loutre
            elif (listepredateur == self.l_loutre):

                if (x > 3):

                    self.nbproies = self.nbproies + random.randint (2,3)

                else :
                    self.nbproies = self.nbproies + random.randint(0,2)
        
        # conditions déclenchant la famine    
        if (listepredateur == self.l_loup):
            if (x <= 2):
                famine()
            
        elif (listepredateur == self.l_loutre):
            if (x <= 3):
                famine()
        
        self.viabilite(listepredateur)

        if (self.nbproies < len(listeproie)):
 
            self.morts_des_animaux(listeproie, self.nbproies)
        
        else :
            # la liste de proie ne peut pas être négative

            # impose une liste vide
            listeproie = []

            self.viabilite(listeproie)

        return listeproie

class EvenementMort(Biocenose):
    ''' Genere les evenements de mort des animaux '''

    def vieillesse(self, liste):

        liste_1 = []
        self.morts_vieillesse = 0

        for i in range(len(liste)):

            liste[i].age = liste[i].age + 1

            if (liste[i].age < liste[i].esperancedevie):

                liste_1.append(liste[i])
                
            else:
                self.morts_vieillesse = self.morts_vieillesse + 1
        
        return liste_1
        
    def chasse_peche(self, liste):

        nb = len(liste)

        # variable de proies mortes par des humains
        self.h_proies = 0
        h_proies1 = float(nb) * 0.2
        self.h_proies = ceil(h_proies1)

        self.morts_des_animaux(liste, self.h_proies)

        self.viabilite(liste)
        
    def predateurs(self, liste):

        nb = len(liste)

        # variable de proies mortes par des prédateurs
        self.pdt_proies = 0
        pdt_proies1 = float(nb)* 0.1
        self.pdt_proies = ceil(pdt_proies1)

        self.morts_des_animaux(liste, self.pdt_proies)
       
        self.viabilite(liste)