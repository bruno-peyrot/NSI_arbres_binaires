class Arbre_binaire:
    """
    Classe permettant d'utiliser des arbres binaires
    """

    def __init__(self, etiquette = None, gauche = None, droit = None):
        """
        arbre = Arbre_binaire()  :  Crée un arbre binaire vide
        arbre = Arbre_binaire('str') : Crée un arbre composé d'un seul noeud
                ayant 'str' comme étiquette
        arbre = Arbre_binaire('str',SAG,SAD) : Crée un arbre binaire dont on
                donne l'étiquette 'str' du noeud racine ainsi que les SAG et
                SAD
        arbre = Arbre_binaire('str',SAG) : Crée un arbre binaire dont on donne
                l'étiquette 'str' du noeud racine ainsi que le SAG, le SAD
                étant vide
        arbre = Arbre_binaire('str',droit=SAD) : Crée un arbre binaire dont on
                donne l'étiquette 'str' du noeud racine ainsi que le SAD, le
                SAG étant vide
        """
        self.__etiquette = etiquette
        self.__gauche = gauche
        self.__droit = droit
        return None

    def __str__(self):
        """
        print(arbre) : Affiche l'arbre binaire passé en argument en se servant
                       de la méthode 'affiche'
                       Affiche 'Arbre vide !' si l'arbre est vide
        """
        self.affiche()
        return ''

    def est_vide(self):
        """
        Renvoie un booléen True si l'arbre binaire est vide, False sinon
        """
        return self.__etiquette is None

    def get_etiquette(self):
        """
        Renvoie l'étiquette du noeud racine de l'arbre binaire
        Renvoie None si l'arbre binaire est vide
        """
        if self == None:
            return None
        else:
            return self.__etiquette

    def set_etiquette(self, nouvelle_etiquette):
        """
        Modifie l'étiquette du noeud racine de l'arbre binaire si celui-ci
        n'est pas vide
        """
        if not(self.est_vide()) and self != None:
            self.__etiquette = nouvelle_etiquette
        return None

    def get_gauche(self):
        """
        Renvoie le SAG de l'arbre binaire.
        Renvoie None si l'arbre binaire ou son SAG est vide
        """
        if not(self.est_vide()) and self != None:
            SAG = self.__gauche
            if SAG == None:
                SAG = Arbre_binaire()
            return SAG
        else:
            return None

    def set_gauche(self, nouveau_SAG):
        """
        Modifie le SAG de l'arbre binaire si celui-ci est non vide
        """
        if not(self.est_vide()) and self != None:
            self.__gauche = nouveau_SAG
            return None

    def get_droit(self):
        """
        Renvoie le SAD de l'arbre binaire.
        Renvoie None si l'arbre binaire ou son SAD est vide
        """
        if not(self.est_vide()) and self != None:
            SAD = self.__droit
            if SAD == None:
                SAD = Arbre_binaire()
            return SAD
        else:
            return None

    def set_droit(self, nouveau_SAD):
        """
        Modifie le SAD de l'arbre binaire si celui-ci est non vide
        """
        if not(self.est_vide()) and self != None:
            self.__droit = nouveau_SAD
            return None

    def taille(self):
        """
        Renvoie la taille de l'arbre binaire
        """
        if self == None or self.est_vide():
            return 0
        else:
            return 1 + Arbre_binaire.taille(self.__gauche) + Arbre_binaire.taille(self.__droit)

    def hauteur(self):
        """
        Renvoie la hauteur de l'arbre binaire
        """
        if self == None or self.est_vide():
            return 0
        else:
            return 1 + max(Arbre_binaire.hauteur(self.__gauche), Arbre_binaire.hauteur(self.__droit))

    def affiche(self):
        """
        Affichage sommaire de l'arbre binaire dans la console Python.
        Affichage de 'Arbre vide !' si l'arbre en question est vide
        """
        if self == None or self.est_vide():
            print('Arbre vide !')
        else:
            file = [self]
            compteur = 0
            noeuds = []
            while compteur < 2 ** self.hauteur() - 1:
                compteur += 1
                arbre = file.pop(0)
                noeuds.append(arbre.get_etiquette())
                arbre_sag = arbre.get_gauche()
                if not(arbre_sag.est_vide()):
                    file.append(arbre_sag)
                else:
                    file.append(Arbre_binaire(' '))
                arbre_sad = arbre.get_droit()
                if not(arbre_sad.est_vide()):
                    file.append(arbre_sad)
                else:
                    file.append(Arbre_binaire(' '))
            for niveau in range(self.hauteur()):
                ligne = noeuds[2 ** niveau - 1 : 2 ** (niveau + 1) - 1]
                espacement = 32 // (2 ** niveau)
                print(' ' * espacement, end = '')
                for colonne in range(len(ligne)):
                    print(str(ligne[colonne]) + ' ' * (2 * espacement - 1), end = '')
                print()
                print()
        return None
