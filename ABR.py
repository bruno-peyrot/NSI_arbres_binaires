class ABR:
    """
    Classe permettant d'utiliser des arbres binaires de recherche
    """

    def __init__(self, valeur = None, gauche = None, droit = None):
        """
        arbre = ABR()  :  Crée un arbre binaire de recherche vide
        arbre = ABR('str') : Crée un arbre binaire de recherche composé d'un
                seul noeud ayant 'str' comme valeur
        arbre = ABR('str',SAG,SAD) : Crée un arbre binaire de recherche dont on
                donne la valeur 'str' du noeud racine ainsi que les SAG et
                SAD
        arbre = ABR('str',SAG) : Crée un arbre binaire de recherche dont on
                donne la valeur 'str' du noeud racine ainsi que le SAG,
                le SAD étant vide
        arbre = ABR('str',droit=SAD) : Crée un arbre binaire de recherche dont
                on donne la valeur 'str' du noeud racine ainsi que le SAD,
                le SAG étant vide
        """
        self.__valeur = valeur
        self.__gauche = gauche
        self.__droit = droit
        return None

    def __str__(self):
        """
        Affiche l'arbre binaire de recherche en se servant de la méthode
        'affiche'
        """
        self.affiche()
        return ''


    def est_vide(self):
        """
        Renvoie un booléen True si l'arbre binaire de recherche est vide,
        False sinon
        """
        return self.__valeur is None

    def get_valeur(self):
        """
        Renvoie la valeur du noeud racine de l'arbre binaire de recherche
        Renvoie None si l'arbre binaire de recherche est vide
        """
        if self == None:
            return None
        else:
            return self.__valeur

    def set_valeur(self, nouvelle_valeur):
        """
        Modifie la valeur du noeud racine de l'arbre binaire de recherche
        si celui-ci n'est pas vide
        """
        if not(self.est_vide()) and self != None:
            self.__valeur = nouvelle_valeur
        return None

    def get_gauche(self):
        """
        Renvoie le SAG de l'arbre binaire de recherche
        Renvoie None si l'arbre binaire de recherche ou son SAG est vide
        """
        if not(self.est_vide()) and self != None:
            SAG = self.__gauche
            if SAG == None:
                SAG = ABR()
            return SAG
        else:
            return None

    def set_gauche(self, nouveau_SAG):
        """
        Modifie le SAG de l'arbre binaire de recherche s'il est non vide
        """
        if not(self.est_vide()) and self != None:
            self.__gauche = nouveau_SAG
            return None

    def get_droit(self):
        """
        Renvoie le SAD de l'arbre binaire de recherche
        Renvoie None si l'arbre binaire de recherche ou son SAD est vide
        """
        if not(self.est_vide()) and self != None:
            SAD = self.__droit
            if SAD == None:
                SAD = ABR()
            return SAD
        else:
            return None

    def set_droit(self, nouveau_SAD):
        """
        Modifie le SAD de l'arbre binaire de recherche s'il est non vide
        """
        if not(self.est_vide()) and self != None:
            self.__droit = nouveau_SAD
            return None

    def taille(self):
        """
        Renvoie la taille de l'arbre binaire de recherche
        """
        if self == None or self.est_vide():
            return 0
        else:
            return 1 + ABR.taille(self.__gauche) + ABR.taille(self.__droit)

    def hauteur(self):
        """
        Renvoie la hauteur de l'arbre binaire de recherche
        """
        if self == None or self.est_vide():
            return 0
        else:
            return 1 + max(ABR.hauteur(self.__gauche), ABR.hauteur(self.__droit))

    def appartient(self, element):
        """
        Renvoie un booléen True si 'element' est présent dans l'arbre binaire
        de recherche, False sinon
        """
        if self == None or self.est_vide():
            return False
        if element < self.get_valeur():
            return self.get_gauche().appartient(element)
        elif element > self.get_valeur():
            return self.get_droit().appartient(element)
        else:
            return True

    def ajoute(self, element):
        """
        Renvoie un nouvel arbre binaire de recherche où 'element' a
        été ajouté
        """
        if self == None or self.est_vide():
            return ABR(element)
        if element < self.get_valeur():
            return ABR(self.get_valeur(), self.get_gauche().ajoute(element), self.get_droit())
        else:
            return ABR(self.get_valeur(), self.get_gauche(), self.get_droit().ajoute(element))

    def minimum(self):
        """
        Renvoie le plus petit élément de l'arbre binaire de recherche,
        celui situé tout en bas à gauche de l'arbre
        """
        if self == None or self.est_vide():
            return None
        if self.get_gauche() == None or self.get_gauche().est_vide():
            return self.get_valeur()
        else:
            return self.get_gauche().minimum()

    def maximum(self):
        """
        Renvoie le plus grand élément de l'arbre binaire de recherche,
        celui situé tout en bas à droite de l'arbre
        """
        if self == None or self.est_vide():
            return None
        if self.get_droit() == None or self.get_droit().est_vide():
            return self.get_valeur()
        else:
            return self.get_droit().maximum()

    def supprime_minimum(self):
        """
        Renvoie un nouvel arbre binaire de recherche où le plus petit
        élément a été supprimé
        """
        if self == None or self.est_vide():
            return ABR()
        if self.get_gauche() == None or self.get_gauche().est_vide():
            return self.get_droit()
        else:
            return ABR(self.get_valeur(), self.get_gauche().supprime_minimum(), self.get_droit())

    def supprime(self, element):
        """
        Renvoie un nouvel arbre binaire de recherche où 'element' a
        été supprimé
        """
        if self == None or self.est_vide():
            return ABR()
        if element < self.get_valeur():
            return ABR(self.get_valeur(), self.get_gauche().supprime(element), self.get_droit())
        elif element > self.get_valeur():
            return ABR(self.get_valeur(), self.get_gauche(), self.get_droit().supprime(element))
        elif self.get_droit() == None or self.get_droit().est_vide():
            return self.get_gauche()
        elif self.get_gauche() == None or self.get_gauche().est_vide():
            return self.get_droit()
        else:
            return ABR(self.get_droit().minimum(), self.get_gauche(), self.get_droit().supprime_minimum())

    def parcours_largeur(self):
        """
        Retourne la liste des noeuds composant l'arbre binaire de recherche
        en suivant l'ordre du parcours en largeur
        """
        if self == None or self.est_vide():
            return None
        else:
            file = [self]
            noeuds = []
            while len(file) != 0:
                arbre = file.pop(0)
                noeuds.append(arbre.get_valeur())
                arbre_sag = arbre.get_gauche()
                if not(arbre_sag.est_vide()):
                    file.append(arbre_sag)
                arbre_sad = arbre.get_droit()
                if not(arbre_sad.est_vide()):
                    file.append(arbre_sad)
        return noeuds

    def parcours_profondeur_prefixe(self):
        """
        Retourne la liste des noeuds composant l'arbre binaire de recherche
        en suivant l'ordre du parcours en profondeur préfixe
        """
        noeuds = []
        if self == None or self.est_vide():
            return []
        else:
            noeuds = noeuds + [self.get_valeur()]
            noeuds = noeuds + self.get_gauche().parcours_profondeur_prefixe()
            noeuds = noeuds + self.get_droit().parcours_profondeur_prefixe()
        return noeuds

    def parcours_profondeur_infixe(self):
        """
        Retourne la liste des noeuds composant l'arbre binaire de recherche
        en suivant l'ordre du parcours en profondeur infixe
        """
        noeuds = []
        if self == None or self.est_vide():
            return []
        else:
            noeuds = noeuds + self.get_gauche().parcours_profondeur_infixe()
            noeuds = noeuds + [self.get_valeur()]
            noeuds = noeuds + self.get_droit().parcours_profondeur_infixe()
        return noeuds

    def parcours_profondeur_suffixe(self):
        """
        Retourne la liste des noeuds composant l'arbre binaire de recherche
        en suivant l'ordre du parcours en profondeur suffixe
        """
        noeuds = []
        if self == None or self.est_vide():
            return []
        else:
            noeuds = noeuds + self.get_gauche().parcours_profondeur_suffixe()
            noeuds = noeuds + self.get_droit().parcours_profondeur_suffixe()
            noeuds = noeuds + [self.get_valeur()]
        return noeuds

    def affiche(self):
        """
        Affichage sommaire de l'arbre binaire de recherche dans
        la console Python
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
                noeuds.append(arbre.get_valeur())
                arbre_sag = arbre.get_gauche()
                if not(arbre_sag.est_vide()):
                    file.append(arbre_sag)
                else:
                    file.append(ABR(' '))
                arbre_sad = arbre.get_droit()
                if not(arbre_sad.est_vide()):
                    file.append(arbre_sad)
                else:
                    file.append(ABR(' '))
            for niveau in range(self.hauteur()):
                ligne = noeuds[2 ** niveau - 1 : 2 ** (niveau + 1) - 1]
                espacement = 32 // (2 ** niveau)
                print(' ' * espacement, end = '')
                for colonne in range(len(ligne)):
                    print(str(ligne[colonne]) + ' ' * (2 * espacement - 1), end = '')
                print()
                print()
        return None

