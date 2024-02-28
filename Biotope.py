from Biocenose import *

class Biotope:
    '''Cette classe est le regroupement de toutes les données de notre ecosysteme'''

    def __init__(self):

        self.Bc = Biocenose()
        self.Ev = EvenementMort()
        self.annees = 0
        
        self.nb_poissons = 0
        self.nb_loutres = 0
        self.nb_loups = 0
        
        self.l_annees = []
        self.l_nbPoisson = []
        self.l_nbLoutre = []
        self.l_nbLoup = []

        self.naissances_poissons = 0
        self.naissances_loutres = 0
        self.naissances_loups = 0
        
        self.morts_poissons = 0
        self.morts_loutres = 0
        self.morts_loups = 0

        self.mort_vieillesse_poissons = 0
        self.mort_vieillesse_loutres = 0
        self.mort_vieillesse_loups = 0

        self.tx_mort_poissons = 0
        self.tx_mort_loutres = 0
        self.tx_mort_loups = 0

        self.tx_nat_poissons = 0
        self.tx_nat_loutres = 0
        self.tx_nat_loups = 0

    def debut(self):
        
        self.Bc.liste_des_animaux(self.Bc.l_poisson, self.nb_poissons)
        self.Bc.liste_des_animaux(self.Bc.l_loutre, self.nb_loutres)
        self.Bc.liste_des_animaux(self.Bc.l_loup, self.nb_loups)

        self.l_annees = [0]
        
        # variables d'initialisation pour le graphique
        self.l_nbPoisson.append(len(self.Bc.l_poisson))
        self.l_nbLoutre.append(len(self.Bc.l_loutre))
        self.l_nbLoup.append(len(self.Bc.l_loup))
        

    def reproductions(self):

        self.naissances_poissons = self.Bc.reproduction(self.Bc.l_poisson)
        self.naissances_loutres = self.Bc.reproduction(self.Bc.l_loutre)
        self.naissances_loups = self.Bc.reproduction(self.Bc.l_loup)

        print( "\n -------------- naissances --------------")

        print("\n nb poissons naissances", self.naissances_poissons)
        print("\n nb loutres naissances", self.naissances_loutres)
        print("\n nb loups naissances", self.naissances_loups)

        
    def consommations(self):

        L1 = self.Bc.consommation(self.Bc.l_loutre, self.Bc.l_poisson)

        self.mort_conso_poissons = self.Bc.nbproies
        self.mort_famine_loutres = self.Bc.morts

        print("\n -------------- consommation loutres --------------")

        print("\n loutres mortes de famine :", self.mort_famine_loutres)
        print("\n Il reste", len(self.Bc.l_loutre), " loutres, du a la famine")
        print ("\n Les loutres mangent ", self.mort_conso_poissons, " poissons")
        
        L2 = self.Bc.consommation(self.Bc.l_loup, self.Bc.l_loutre)

        self.mort_conso_loutres = self.Bc.nbproies
        self.mort_famine_loups = self.Bc.morts

        print("\n -------------- consommation loups --------------")

        print("\n loups morts de famine :", self.mort_famine_loups)
        print("\n Il reste", len(self.Bc.l_loup), " loups, du a la famine")
        print("\n Les loups mangent ", self.mort_conso_loutres, " loutres")
        
        
        self.Bc.l_poisson = L1
        self.Bc.l_loutre = L2

        print("\n nb poissons vivants après conso : ", len(L1),"\n nb loutres vivantes après conso : ", len(L2))
        
        
    def pecher(self):
            
            self.Ev.chasse_peche(self.Bc.l_poisson)

            print("\n Nb poissons vivants après pêche : ", len(self.Bc.l_poisson))
            self.peche_poissons = self.Ev.h_proies

            
    def chasser_lt(self):
            
            self.Ev.chasse_peche(self.Bc.l_loutre)

            print("\n Nb loutres vivantes après chasse : ", len(self.Bc.l_loutre))
            self.chasse_loutres = self.Ev.h_proies

            
    def chasser_lp(self):
        
            self.Ev.chasse_peche(self.Bc.l_loup)

            print("\n Nb loups vivants après chasse : ", len(self.Bc.l_loup))
            self.chasse_loups = self.Ev.h_proies


    def morts_predateurs(self):

        print("\n -------------- prédation externe --------------")

        self.Ev.predateurs(self.Bc.l_poisson)
        print("\n Nb poissons après prédateurs :", len(self.Bc.l_poisson))

        self.pred_poissons = self.Ev.pdt_proies
        print("\n Nb de poissons mangés par les pred :", self.pred_poissons)
        
        self.Ev.predateurs(self.Bc.l_loutre)
        print("\n Nb loutres apres prédateurs :", len(self.Bc.l_loutre))

        self.pred_loutres = self.Ev.pdt_proies
        print("\n Nb de loutres mangées par les pred :", self.pred_loutres, "\n")
    
    def mort_vieillesse(self):

        print("\n -------------- morts vieillesse --------------")

        self.Bc.l_poisson = self.Ev.vieillesse(self.Bc.l_poisson)
        self.mort_vieillesse_poissons = self.Ev.morts_vieillesse
        self.Bc.viabilite(self.Bc.l_poisson)
        print ("\n Poissons morts vieillesse : ", self.mort_vieillesse_poissons)
        self.Bc.viabilite(self.Bc.l_poisson)
        
        self.Bc.l_loutre = self.Ev.vieillesse(self.Bc.l_loutre)
        self.mort_vieillesse_loutres = self.Ev.morts_vieillesse
        self.Bc.viabilite(self.Bc.l_loutre)
        print ("\n Loutres morts vieillesse : ", self.mort_vieillesse_loutres)
        self.Bc.viabilite(self.Bc.l_loutre)
        
        self.Bc.l_loup = self.Ev.vieillesse(self.Bc.l_loup)
        self.mort_vieillesse_loups = self.Ev.morts_vieillesse
        self.Bc.viabilite(self.Bc.l_loup)
        print ("\n Loups morts vieillesse : ", self.mort_vieillesse_loups)
        self.Bc.viabilite(self.Bc.l_loup)
    
    random.seed(3)
    def annee(self):
        
        self.annees += 1
        self.l_annees.append(self.annees)
        self.peche_poissons = 0
        self.chasse_loutres = 0
        self.chasse_loups = 0

        print("\n -------------- Nouvelle année --------------")

        print ("\n Nous sommes à l'année :", self.annees)
        
        print("\n -------------- initialisation --------------")
        
        print ("\n nb de loups au début :", len(self.Bc.l_loup))
        print ("\n nb de loutres au début :", len(self.Bc.l_loutre))
        print ("\n nb de poissons au début :", len(self.Bc.l_poisson))

        self.mort_vieillesse()

        if (self.stop() != True) :
            
            self.reproductions()

            print ("\n nb loups après naissances :", len(self.Bc.l_loup))
            print ("\n nb de loutres après naissances :", len(self.Bc.l_loutre))
            print ("\n nb de poissons après naissances :", len(self.Bc.l_poisson))
            
            self.consommations()
            
            self.morts_predateurs()

            self.stop()
         
        else :
            pass

    def compteur(self):

        self.l_nbPoisson.append(len(self.Bc.l_poisson))
        self.l_nbLoutre.append(len(self.Bc.l_loutre))
        self.l_nbLoup.append(len(self.Bc.l_loup))

        self.nb_poissons = len(self.Bc.l_poisson)
        self.nb_loutres = len(self.Bc.l_loutre)
        self.nb_loups = len(self.Bc.l_loup)

        print("\n -------------- fin d'année --------------")

        print ("\n nb poissons à l'année ", self.annees , " : " ,len(self.Bc.l_poisson))
        print ("\n nb loutres à l'année ", self.annees , " : " , len(self.Bc.l_loutre))
        print ("\n nb loups à l'année ", self.annees , " : " , len(self.Bc.l_loup))

        print ("\n -------------- bilan de l'année -------------- \n")

        self.morts_poissons = self.mort_vieillesse_poissons + self.mort_conso_poissons + self.pred_poissons + self.peche_poissons
        print (self.morts_poissons, " poissons sont morts cette année \n")

        self.morts_loutres = self.mort_vieillesse_loutres + self.pred_loutres + self.mort_conso_loutres + self.chasse_loutres + self.mort_famine_loutres
        print (self.morts_loutres, " loutres sont mortes cette année \n")

        self.morts_loups = self.mort_vieillesse_loups + self.chasse_loups + self.mort_famine_loups
        print (self.morts_loups, " loups sont morts cette année \n")

    def taux(self):

        self.tx_mort_poissons = floor((self.morts_poissons/(self.nb_poissons + (self.morts_poissons/2))) * 100)
        self.tx_mort_loutres = floor((self.morts_loutres/(self.nb_loutres + (self.morts_loutres/2))) * 100)
        self.tx_mort_loups = floor((self.morts_loups/(self.nb_loups + (self.morts_loups/2))) * 100)

        print("-------------- Taux mortalité --------------")

        print (self.tx_mort_poissons, " : taux de mortalité poisson \n")
        print (self.tx_mort_loutres, " : taux de mortalité loutre \n")
        print (self.tx_mort_loups, " : taux de mortalité loup \n")

        self.tx_nat_poissons = floor((self.naissances_poissons/(self.nb_poissons + (self.morts_poissons/2))) * 100)
        self.tx_nat_loutres = floor((self.naissances_loutres/(self.nb_loutres + (self.morts_loutres/2))) * 100)
        self.tx_nat_loups = floor((self.naissances_loups/(self.nb_loups + (self.morts_loups/2))) * 100)

        print("-------------- Taux natalité --------------")

        print(self.tx_nat_poissons, " : taux de natalité poisson \n")
        print(self.tx_nat_loutres, " : taux de natalité loutre \n")
        print(self.tx_nat_loups, " : taux de natalité loup \n")

    def stop(self):

        espece_eteinte_p = self.Bc.viabilite(self.Bc.l_poisson)
        espece_eteinte_lt = self.Bc.viabilite(self.Bc.l_loutre)
        espece_eteinte_lp = self.Bc.viabilite(self.Bc.l_loup)

        if ((espece_eteinte_p == True) or (espece_eteinte_lt == True) or (espece_eteinte_lp == True)) :
            return True