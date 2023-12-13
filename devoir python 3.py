class Carte:
    def __init__(self,essence, name, describe):
        self.__mana=essence
        self.__nom=name
        self.__description=describe
    
    def getMana(self):
        return self.__mana
    
    def getNom(self):
        return self.__nom
    
    def getDescritption(self):
        return self.__description
    
class Mage:
    def __init__(self,name,life,essence):
        self.__nom=name
        self.__vie=life
        self.__mana=essence
        self.__manatotal=100
        self.__main={1:Cristal,2:Creature,3:Blast}
        self.__defausse={}
        self.__zonedejeu={}

    def getNom(self):
        return self.__nom
    
    def getVie(self):
        return self.__vie
    
    def getMana(self):
        return self.__mana
    
    def getMain(self):
        return self.__main
    
    def getDefausse(self):
        return self.__defausse
    
    def getzonedejeu(self):
        return self.__zonedejeu
    

    def jouer(self):
        cartejoué=int(input("vous possédez actuellement",self.__main,", que souhaitez vous jouer?"))
        self.__main-=self.__main[cartejoué]
        self.__zonedejeu+=self.__main[cartejoué]

        return cartejoué

    def augmentationmanatotal(self,valeur):
        self.__manatotal+=valeur

    #a utiliser en fin de boucle
    def recuperation(self):
        self.__mana=self.__manatotal


class Cristal(Carte):
    def __init__(self,essence, name, describe):
        Carte.__init__(self, essence, name, describe)
        self.__valeurmana=7

    def getValeur(self):
        return self.__valeurmana
    
    def cartejoué(self):
        if (int(Mage.jouer())=1):
            Mage.augmentationmanatotal(self,7)



class Creature(Carte):
    def __init__(self,essence,name,describe):
        Carte.__init__(self, essence, name, describe)

        self.__vie=50

        self.__attaque=10

    def getPV(self):
        return self.__vie
    
    def getAttaque(self):
        return self.__attaque
    
    def  joué(self):
        Mage.getMana-=Carte.getMana

        Mage.getMain-=Mage.getMain[Mage.jouer()]
        Mage.getMain+=Mage.getMain[Mage.jouer()]

    def attaque(self):
        #attaque une créature ou un mage, si c'est une créature alors il subit des dégats en retour

    def mort(self):
        if (self.__vie<=0):
            Mage.getzonedejeu-=Creature
            Mage.getDefausse+=Creature
            #la creature sors de la zone de jeu et va dans la pile de défausse


class Blast(Carte):
    def __init__(self,essence,name,describe):
        Carte.__init__(self, essence, name, describe)
        self.__valeurmana=9

    def getValeur(self):
        return self.__valeurmana

    def utilisationcreature(self):
        Creature.getPV-=self.__valeurmana

        Mage.getMain-=Mage.getMain[Mage.jouer()]
        Mage.getDefausse+=Mage.getMain[Mage.jouer()]

    def utilisationmage(self):
        Mage.getVie-=self.__valeurmana

        Mage.getMain-=Mage.getMain[Mage.jouer()]
        Mage.getDefausse+=Mage.getMain[Mage.jouer()]





