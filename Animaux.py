import random

class Animal:

    def __init__(self, nom, ID, age, esperance):
        ''' Constructeur créant l'animal'''

        self.nom = nom
        self.id = ID
        self.esperancedevie = esperance
        self.age = age
        self.sexe = random.randint(0, 1)
        
    def __str__(self) :
        return f" | ID : {self.id} | Sexe : {self.sexe} | Age : {self.age} | Esperance de vie :{self.esperancedevie}"
   
    def get_nom(self):
        return(self.nom)
    
    def get_ID(self):
        return(self.id)
    
    def get_age(self):
        return(self.age)

    def get_esperancedevie(self):
        return(self.esperancedevie)

    def get_sexe(self):
        return(self.sexe)

# -------------------------------------------------------
# Classe de chaque Animal 

class Loup(Animal):

    def __init__(self, age):

        esperance = random.randint(12, 15)

        if age == -1 :
            
            age = random.randint(0,esperance-1)

        else :
            age = 0
        
        super().__init__("Loup", 0, age, esperance)

    def __str__(self) :
        return ("Loup" + super().__str__())

class Loutre(Animal) :

    def __init__(self, age):

        esperance = random.randint(8, 12)

        if age == -1 :
            
            age = random.randint(0,esperance-1)

        else :
            age = 0
        
        super().__init__("Loutre", 0, age, esperance)

    def __str__(self) :
        return ("Loutre" + super().__str__())

class Poisson(Animal) :
    
    def __init__(self, age):

        esperance = random.randint(4, 6)

        if age == -1 :
            
            age = random.randint(0,esperance-1)

        else :
            age = 0
        
        super().__init__("Poisson", 0, age, esperance)

    def __str__(self) :
        return ("Poisson" + super().__str__())