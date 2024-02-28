from Biotope import *
import numpy as np
import pylab, pygame, sys, json, random
import matplotlib
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Renderer():

    def start(self):
        ''' fenêtre d'entrée d'un nom'''
        start = Tk()
        #start.iconbitmap("pictures/ecosystem.ico")
        start.title("Debut du jeu")
        start.geometry("300x150")

        # positionnement de la fenêtre sur l'écran
        screen_x = int(start.winfo_screenwidth())
        screen_y = int(start.winfo_screenwidth())
        window_x = 300
        window_y = 150
        posX = (screen_x // 2) - (window_x // 2)
        posY = (screen_y // 4) - (window_y // 2)
        geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
        start.geometry(geo)

        self.nom=''
        
        def verification():
            if(self.saisie_nom.get() == ''):
                messagebox.showerror("Erreur","Vous n'avez mis aucun nom")

            else:
                print("je valide", self.saisie_nom.get())
                self.nom = str(self.saisie_nom.get())
                start.destroy()
                R.principal()

        # frame / labelframe
        startframe = Frame(start, bg = 'white', bd = 1, highlightthickness = 0, relief = SUNKEN)
        startframe.pack(expand = 1)
        labl_debut = LabelFrame(startframe, text =  " Bonjour, vous entrez dans la simulation.\n Veuillez entrer votre nom.")
        labl_debut.grid()
        labl_debut.pack(expand = 1)

        # variable de nom 
        nom = StringVar()
        self.saisie_nom = Entry(labl_debut, textvariable = nom.get())
        self.saisie_nom.pack()

        # bouton
        btn_valid = Button(labl_debut, text = "Valider", command = verification)
        btn_valid.pack(expand = 1)
        
        start.mainloop()
    
    def principal(self):
        # valeurs initiales
        self.B = Biotope()
        # création de la fenêtre
        self.window = Tk()
        self.window.title("Biocénose")
        self.window.geometry("1158x699")
        #self.window.iconbitmap("pictures/ecosystem.ico")
        
        self.window.maxsize(1158,699)
        self.window.minsize(1158,699)

        screen_x = int(self.window.winfo_screenwidth())
        screen_y = int(self.window.winfo_screenwidth())
        window_x = 1158
        window_y = 699
        posX = (screen_x // 2) - (window_x // 2)
        posY = (screen_y // 4) - (window_y // 2)
        geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
        self.window.geometry(geo)
# ----------------------------------------------------------------------------------------------------------------------------------------------------
    # Methodes
        def _quit():
            self.window.quit()     
            self.window.destroy()
            
        def restart_game():
            self.window.destroy()
            self.start()

        def attention():
            messagebox.showinfo("Here's comes a New Challenger !", "Bonjour à toi " + self.nom +" !\nBienvenu dans Coloc'system " + "\nN'oublie pas d'aller lire les règles, accessibles en haut à gauche de ton écran.", icon = 'info')
        attention()

        def quitter():
            MsgBox = messagebox.askquestion('Quitter','Souhaitez-vous partir?', icon = 'question')
            if MsgBox == 'yes':
                _quit()
            else:
                messagebox.showinfo("Sage décision !",'Bon retour parmis nous !')

        def valider():
            
            # valeurs d'initialisation donné par le joueur
            self.B.nb_poissons = int(nombre_poissons.get())
            self.B.nb_loutres = int(nombre_loutres.get())
            self.B.nb_loups = int(nombre_loups.get())

            btn_valider.config(state = DISABLED)
            btn_annee.config(state = NORMAL)

            self.B.debut()
                
        def add_scores():
            self.ouvrir = open('Programme/scores.json')
            self.data = json.load(self.ouvrir)

            # recupere les données du dictionnaire dans json
            self.json_nom = self.data["nom"]
            self.json_score = self.data["score"]

            if int(self.json_score) < int(self.new_annee.get()):
                scores = {"nom" : self.nom,
                        "score" : self.new_annee.get()}

                # remplace l'ancienne valeur par la nouvelle
                with open('scores.json', 'w') as f_write:
                    json.dump(scores, f_write)
                return True

        def arret():
            messagebox.showerror("Game Over", "L'écosystème n'est plus viable! \n Vous avez tenu : " + str(self.new_annee.get()) + " années", icon = 'warning')

            if(add_scores() == True):
                messagebox.showinfo('Super !', self.nom + ', vous avez réalisé le meilleur score !' )

            msgbox = messagebox.askretrycancel("Recommencer", "Que voulez vous faire ?", icon = 'question')

            if msgbox == True:
                restart_game()
            else:
                _quit()

        def info():
            # fenêtre primaire
            info = Tk()
            #info.iconbitmap("pictures/ecosystem.ico")
            info.title("Règles du Jeu")
            info.geometry("1100x300")

            with open("Fiches/Regles.txt", encoding = 'utf-8') as file:
                content = file.read()
  
            Label(info, text = content).pack(padx = 10, pady = 10)
            screen_x = int(self.window.winfo_screenwidth())
            screen_y = int(self.window.winfo_screenwidth())
            window_x = 1120
            window_y = 350
            posX = (screen_x // 2) - (window_x // 2)
            posY = (screen_y // 4) - (window_y // 2)
            geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
            info.geometry(geo)
        
        def fiche_loup():
            # fenêtre primaire
            info = Tk()
            #info.iconbitmap("pictures/ecosystem.ico")
            info.title("Fiche informative : LOUP")
            info.geometry("700x150")

            with open("Fiches/Loups.txt", encoding = 'utf-8') as file:
                content = file.read()
  
            Label(info, text = content).pack(padx = 10, pady = 10)
            screen_x = int(self.window.winfo_screenwidth())
            screen_y = int(self.window.winfo_screenwidth())
            window_x = 800
            window_y = 150
            posX = (screen_x // 2) - (window_x // 2)
            posY = (screen_y // 4) - (window_y // 2)
            geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
            info.geometry(geo)
        
        def fiche_loutre():
            # fenêtre primaire
            info = Tk()
            #info.iconbitmap("pictures/ecosystem.ico")
            info.title("Fiche informative : LOUTRE")
            info.geometry("500x300")

            with open("Fiches/Loutres.txt", encoding = 'utf-8') as file:
                content = file.read()
  
            Label(info, text = content).pack(padx = 10, pady = 10)
            screen_x = int(self.window.winfo_screenwidth())
            screen_y = int(self.window.winfo_screenwidth())
            window_x = 800
            window_y = 150
            posX = (screen_x // 2) - (window_x // 2)
            posY = (screen_y // 4) - (window_y // 2)
            geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
            info.geometry(geo)
            
        
        def fiche_poisson():
            # fenêtre primaire
            info = Tk()
            #info.iconbitmap("pictures/ecosystem.ico")
            info.title("Fiche informative : POISSON")
            info.geometry("500x300")

            with open("Fiches/Poissons.txt", encoding = 'utf-8') as file:
                content = file.read()
            
            Label(info, text = content).pack(padx = 10, pady = 10)
            screen_x = int(self.window.winfo_screenwidth())
            screen_y = int(self.window.winfo_screenwidth())
            window_x = 800
            window_y = 160
            posX = (screen_x // 2) - (window_x // 2)
            posY = (screen_y // 4) - (window_y // 2)
            geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
            info.geometry(geo)
            
        def fiche_interactions():
            # fenêtre primaire
            info = Tk()
            #info.iconbitmap("pictures/ecosystem.ico")
            info.title("Fiche informative : INTERACTIONS DE COLOC'SYSTÈME")
            info.geometry("500x300")

            with open("Fiches/interactions.txt", encoding = 'utf-8') as file:
                content = file.read()
            
            Label(info, text = content).pack(padx = 10, pady = 10)
            screen_x = int(self.window.winfo_screenwidth())
            screen_y = int(self.window.winfo_screenwidth())
            window_x = 1000
            window_y = 250
            posX = (screen_x // 2) - (window_x // 2)
            posY = (screen_y // 4) - (window_y // 2)
            geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
            info.geometry(geo)
                
        def show_about():
            # seconde fenêtre primaire
            about_window = Toplevel(self.window)
            #about_window.iconbitmap("pictures/ecosystem.ico")
            about_window.title("A propos")
            lbjeu = Label(about_window, text = "Coloc'système a été créé en mars 2021,\n Par : Adji Faty Dieng, Aude Bernier, Jonas Bertoli et Samara Frachet.")
            lbjeu.pack()

        # principaux menu
        menubar = Menu(self.window)

        first_menu = Menu(menubar, tearoff = 0)
        second_menu= Menu(menubar, tearoff = 0)

        menubar.add_cascade(label = "Jeu", menu = first_menu)
        menubar.add_cascade(label = "Informations", menu = second_menu)
        menubar.add_command(label = "Quitter", command = quitter)

        first_menu.add_command(label = "Règles", command = info)
        first_menu.add_separator()
        first_menu.add_command(label = "A propos", command = show_about)
        second_menu.add_command(label = "Infos Loups", command = fiche_loup)
        second_menu.add_separator()
        second_menu.add_command(label = "Infos Loutres", command = fiche_loutre)
        second_menu.add_separator()
        second_menu.add_command(label = "Infos Poissons", command = fiche_poisson)
        second_menu.add_separator()
        second_menu.add_command(label = "Infos Interactions", command = fiche_interactions)

        self.window.config(menu = menubar)
 
        # cadre des modules
        moduleframe = Frame(self.window, width = 600, borderwidth = 1, bd = 1, highlightthickness = 0, relief = SUNKEN)
        moduleframe.config(background = "gray")
        moduleframe.grid(row = 0, column = 0, sticky = 's')

        # cadre du graphique
        graphbox = Frame(self.window, width = 600, borderwidth=1, bd = 1,highlightthickness = 0, relief = SUNKEN)
        graphbox.config(background = "white")
        graphbox.grid(row = 0, column = 1, sticky = 's')

        # cadre des actions
        actframe = Frame(graphbox)
        actframe.grid(row = 0, column = 0)

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    # LABELFRAME/LABEL INITIALISATION

        # Labelframe initialisation 
        initialisation = LabelFrame(moduleframe, text = "Initialisation ", padx = 20, pady = 20)
        initialisation.grid(row = 0, column = 0, sticky = 'ew')

        # séparation des animaux en label
        labl_loups = Label(initialisation, text =  "Loups")
        labl_loups.grid(row = 0, column = 0)
        labl_loutres = Label(initialisation, text =  "Loutres")
        labl_loutres.grid(row = 1, column = 0)
        labl_poissons = Label(initialisation, text =  "Poissons")
        labl_poissons.grid(row = 2, column = 0)
        
        # saisies des animaux ( revoir le max et le min )
        nombre_loups = Spinbox(initialisation, from_= 3, to = 7)
        nombre_loutres = Spinbox(initialisation, from_= 30, to = 80)
        nombre_poissons = Spinbox(initialisation, from_= 100, to = 500)
        nombre_loups.grid(row = 0, column = 1)
        nombre_loutres.grid(row = 1, column = 1)
        nombre_poissons.grid(row = 2, column = 1)
        # ACTIONS
        #LabelFrame Pricipal
        Actions = LabelFrame(actframe, text = "Actions")
        Actions.grid(row = 0,column = 0)
        
        # variables
        var_choix_chasse_loups = IntVar()
        var_choix_chasse_loutres = IntVar()
        var_choix_peche = IntVar()
        
        # labelframe Chasse / Pêche 
        Chasse = LabelFrame(Actions, text = "Chasse")
        Chasse.grid(row = 1, column = 1, rowspan = 3, sticky = W)
        Peche = LabelFrame(Actions, text = "Pêche")
        Peche.grid(row = 4, column = 1, sticky = W)

        # labelframe Chasse\Loups, Chasse\Loutres et Pêche\Poissons
        chasse_loups = LabelFrame(Chasse, text = "Loups")
        chasse_loups.grid(row = 0, column = 1, rowspan = 3)
        chasse_loutres = LabelFrame(Chasse, text = "Loutres")
        chasse_loutres.grid(row = 0, column = 2, rowspan = 3)
        peche_poissons = LabelFrame(Peche, text = "Poissons")
        peche_poissons.grid(row = 0, column = 0)
        
        # choix chasse loups/loutres
        oui_chasse_loups = Radiobutton(chasse_loups, text = "Oui", value = 1, variable = var_choix_chasse_loups)
        non_chasse_loups = Radiobutton(chasse_loups, text = "Non", value = 2, variable = var_choix_chasse_loups)
        oui_chasse_loutres = Radiobutton(chasse_loutres, text = "Oui", value = 3, variable = var_choix_chasse_loutres)
        non_chasse_loutres = Radiobutton(chasse_loutres, text = "Non", value = 4, variable = var_choix_chasse_loutres)
        oui_chasse_loups.pack()
        non_chasse_loups.pack()
        oui_chasse_loutres.pack()
        non_chasse_loutres.pack()

        # choix Pêche
        oui_peche = Radiobutton(peche_poissons, text = "Oui", value = 5, variable = var_choix_peche)
        non_peche = Radiobutton(peche_poissons, text = "Non", value = 6, variable = var_choix_peche)
        
        oui_peche.grid()
        non_peche.grid()

        #Valeurs par défaut
        var_choix_chasse_loups.set(2)
        var_choix_chasse_loutres.set(4)
        var_choix_peche.set(6)

        # labelframe année
        Annees = LabelFrame(moduleframe, text = " Années   ", padx = 20, pady = 5)
        Annees.grid(row = 1, column = 0, sticky = 'ew')
        self.new_annee = StringVar()
        self.new_annee.set(self.B.annees)
        self.labAnnee = Label(Annees, text = "Année : " + str(self.new_annee.get()))
        self.labAnnee.pack()

        # labelframe animaux
        Poissons = LabelFrame(moduleframe, text = " Poissons   ", padx = 20, pady = 15)
        Poissons.grid(row = 2, column = 0, sticky = 'ew')
        Loutres = LabelFrame(moduleframe, text = " Loutres   ", padx = 20, pady = 15)
        Loutres.grid(row = 3, column = 0, sticky = 'ew')
        Loups = LabelFrame(moduleframe, text = " Loups   ", padx = 20, pady = 15)
        Loups.grid(row = 4, column = 0, sticky = 'ew')

        # valeurs du dictionnaire scores json
        self.ouvrir = open("Programme/scores.json")
        self.data = json.load(self.ouvrir)
        self.json_nom = self.data['nom']
        self.json_score = self.data['score']
        high_score = LabelFrame(moduleframe, text = " Meilleur score    ", padx = 20, pady = 15)
        high_score.grid(row = 5, column = 0, sticky = 'sew')
        lab_h_score = Label(high_score, text = self.json_nom + " est le meilleur joueur avec un score de : " + self.json_score + ' années.' )
        lab_h_score.pack()
        
        # INFORMATIONS SUR L'EVOLUTION DE L'ECOSYSTEME

        # variables poisson
        self.nbr_p = StringVar()
        self.tx_mortsP = StringVar()
        self.new_p = StringVar()
        self.nb_mortsP = StringVar()
        self.tx_natP = StringVar()
        self.nbr_p.set(self.B.nb_poissons)
        self.tx_mortsP.set(self.B.tx_mort_poissons)
        self.tx_natP.set(self.B.tx_nat_poissons)
        self.new_p.set(self.B.naissances_poissons)
        self.nb_mortsP.set(self.B.morts_poissons)

        # variables loutre
        self.nbr_lt = StringVar()
        self.tx_mortsLt = StringVar()
        self.tx_natLt = StringVar()
        self.nb_mortsLt = StringVar()
        self.new_lt = StringVar()
        
        self.nbr_lt.set(self.B.nb_loutres)
        self.tx_mortsLt.set(self.B.tx_mort_loutres)
        self.tx_natLt.set(self.B.tx_nat_loutres)
        self.nb_mortsLt.set(self.B.morts_loutres)
        self.new_lt.set(self.B.naissances_loutres)

        # variables loup
        self.nbr_lp = StringVar()
        self.tx_mortsLp = StringVar()
        self.tx_natLp = StringVar()
        self.nb_mortsLp = StringVar()
        self.new_lp = StringVar()

        self.nbr_lp.set(self.B.nb_loups)
        self.tx_mortsLp.set(self.B.tx_mort_loups)
        self.tx_natLp.set(self.B.tx_nat_loups)
        self.nb_mortsLp.set(self.B.morts_loups)
        self.new_lp.set(self.B.naissances_loups)

        # affichage variables sur LabelFrame
        self.labP = Label(Poissons, text = str(self.nbr_p.get()) + " : Nombre de Poissons\n " + str(self.new_p.get()) + " : Nombre de naissances\n" + str(self.nb_mortsP.get()) + " : Nombre de décès\n" + str(self.tx_natP.get()) + "% : Taux de natalités\n" + str(self.tx_mortsP.get()) + "% : Taux de Mortalité" )
        self.lablt = Label(Loutres, text = str(self.nbr_lt.get()) + " : Nombre de Loutres\n " + str(self.new_lt.get()) + " : Nombre de naissances\n" + str(self.nb_mortsLt.get()) + " : Nombre de décès\n" + str(self.tx_natLt.get()) + "% : Taux de natalités\n" + str(self.tx_mortsLt.get()) + "% : Taux de Mortalité" )
        self.lablp = Label(Loups, text = str(self.nbr_lp.get()) + " : Nombre de Loups\n " + str(self.new_lp.get()) + " : Nombre de naissances\n" + str(self.nb_mortsLp.get()) + " : Nombre de décès\n" + str(self.tx_natLp.get()) + "% : Taux de natalités\n" + str(self.tx_mortsLp.get()) +"% : Taux de Mortalité")
        
        self.labP.pack()
        self.lablt.pack()
        self.lablp.pack()
#--------------------------------------------------------------------------------------------------------------------------------------
    # GRAPHIQUE
        # Figure axe graphique
        self.fig = Figure(figsize = [8, 5], facecolor = 'xkcd:dark')
        self.ax = self.fig.add_subplot(111)
    
        # Configurations du graphique  
        self.ax.set_facecolor('xkcd:dark')
        self.ax.set_title("Biocénose", color = 'white')

        # couleurs des axes
        self.ax.spines['top'].set_color('white')
        self.ax.spines['right'].set_color('white')
        self.ax.spines['left'].set_color('white')
        self.ax.spines['bottom'].set_color('white')
        self.ax.tick_params(axis = 'both', colors = 'white')

        # emplacement du graph
        self.canvas = FigureCanvasTkAgg(self.fig, master = graphbox)
        self.canvas.get_tk_widget().grid(row = 1, column = 0, sticky = 'nwse')
        
        # Tracés des courbes
        Loup, = self.ax.plot(self.B.l_annees, self.B.l_nbLoup, linewidth = 2.0, label = 'Loups', color = 'gray')
        Loutre, = self.ax.plot(self.B.l_annees, self.B.l_nbLoutre, linewidth = 2.0, label = 'Loutres', color = 'brown')
        Poisson, = self.ax.plot(self.B.l_annees, self.B.l_nbPoisson, linewidth = 2.0, label = 'Poissons', color = 'blue')
        self.fig.legend(handles=(Loup, Loutre, Poisson),labels=('Loups', 'Loutres', 'Poissons'),loc='upper right')
        
        self.canvas.draw()
        
        def update():

            if(self.B.stop() == True):
                arret()

            # lancement du programme
            self.B.annee()

            # Activation Chasse/Peche regulatrice
            var_chasselp = var_choix_chasse_loups.get()
            if var_chasselp == 1:
                self.B.chasser_lp()

            var_chasselt = var_choix_chasse_loutres.get()
            if var_chasselt == 3:
                print("La chasse loutre est active")
                self.B.chasser_lt()
            var_peche = var_choix_peche.get()
            
            if var_peche == 5:
                print("La peche est active")
                self.B.pecher()

            self.B.compteur()
            self.B.taux()

            # Configuration du graphique  
            self.ax.set_facecolor('xkcd:dark')
            self.ax.set_title("Biocénose", color = 'white')
                
            self.ax.spines['top'].set_color('white')
            self.ax.spines['right'].set_color('white')
            self.ax.spines['left'].set_color('white')
            self.ax.spines['bottom'].set_color('white')

            self.ax.tick_params(axis = 'both', colors = 'white')

            # Tracé des courbes 
            Loup, = self.ax.plot(self.B.l_annees, self.B.l_nbLoup, linewidth = 2.0, label = 'Loups', color = 'gray')
            Loutre, = self.ax.plot(self.B.l_annees, self.B.l_nbLoutre, linewidth = 2.0, label = 'Loutres', color = 'brown')
            Poisson, = self.ax.plot(self.B.l_annees, self.B.l_nbPoisson, linewidth = 2.0, label = 'Poissons', color = 'blue')

            # Légende du graph
            self.fig.legend(handles=(Loup, Loutre, Poisson),labels=('Loups', 'Loutres', 'Poissons'),loc='upper right')
            
            # intégration du graphique 
            self.canvas.get_tk_widget().grid(row = 1, column = 0, sticky = 'nwse')
            self.canvas.draw()
            self.new_annee.set(self.B.annees)
            self.labAnnee.configure(text = "Année : " + str(self.new_annee.get()))
            
            # Variables modifiées 
            self.nbr_p.set(self.B.nb_poissons)
            self.tx_mortsP.set(self.B.tx_mort_poissons)
            self.tx_natP.set(self.B.tx_nat_poissons)
            self.new_p.set(self.B.naissances_poissons)
            self.nb_mortsP.set(self.B.morts_poissons)

            self.nbr_lt.set(self.B.nb_loutres)
            self.tx_mortsLt.set(self.B.tx_mort_loutres)
            self.tx_natLt.set(self.B.tx_nat_loutres)
            self.nb_mortsLt.set(self.B.morts_loutres)
            self.new_lt.set(self.B.naissances_loutres)

            self.nbr_lp.set(self.B.nb_loups)
            self.tx_mortsLp.set(self.B.tx_mort_loups)
            self.tx_natLp.set(self.B.tx_nat_loups)
            self.nb_mortsLp.set(self.B.morts_loups)
            self.new_lp.set(self.B.naissances_loups)

            # affichage nouvelles variables
            self.labP.configure(text = str(self.nbr_p.get()) + " : Nombre de Poissons\n " + str(self.new_p.get()) + " : Nombre de naissances\n" + str(self.nb_mortsP.get()) + " : Nombre de décès\n" + str(self.tx_natP.get()) + "% : Taux de natalités\n" + str(self.tx_mortsP.get()) + "% : Taux de Mortalité" )
            self.lablt.configure(text = str(self.nbr_lt.get()) + " : Nombre de Loutres\n " + str(self.new_lt.get()) + " : Nombre de naissances\n" + str(self.nb_mortsLt.get()) + " : Nombre de décès\n" + str(self.tx_natLt.get()) + "% : Taux de natalités\n" + str(self.tx_mortsLt.get()) + "% : Taux de Mortalité")
            self.lablp.configure(text = str(self.nbr_lp.get()) + " : Nombre de Loups\n " + str(self.new_lp.get()) + " : Nombre de naissances\n" + str(self.nb_mortsLp.get()) + " : Nombre de décès\n" + str(self.tx_natLp.get()) + "% : Taux de natalités\n" + str(self.tx_mortsLp.get()) +"% : Taux de Mortalité")
            
            if(self.B.stop() == True):
                arret()

                
        # BOUTONS 
        btn_annee = Button(actframe, text = "Passer à l'année suivante", state = DISABLED, command = update)
        btn_annee.grid(row = 0, column = 1, ipadx = 269, ipady = 84)
    
        btn_valider = Button(initialisation, text = "Ok", command = valider)
        btn_valider.grid(row = 3, column = 4, sticky = E, ipadx = 30, ipady = 20, padx = 20)
        self.window.mainloop()

if __name__ == "__main__": 
    R = Renderer()
    R.start()