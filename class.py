class Dictionnary:
    """Une classe dictionnaire ordonnees:
    Dictionnary(dict(),**dictionaire)"""

    def __init__(self,base={},**dictionnaire):
        try:
                self._listKey=list(base.keys())
                self._listValue=list(base.values())
                self._listKey.extend(list(dictionnaire.keys()))
                self._listValue.extend(list(dictionnaire.values()))
        except AttributeError:
            print("L'attribut n'est pas correcte!!\nCan be much information")
    def __getitem__(self,cle):
        """On surcharge l'operateur [],une methode get"""
        try:
            i=self._listKey.index(cle)
        except ValueError:
            str_error="Error:this key is not correct"
            return str_error
        else:
            return self._listValue[i]
    def __setitem__(self,cle,value):
        #On surcharge l'operateur [],une methode set

        if self._listKey.count(cle)==1:#Si la cle existe on ecrase sa valeur et on la remplace
            i=self._listKey.index(cle)
            del self._listValue[i]
            self._listValue.insert(i,value)
        elif self._listKey.count(cle)==0:
            #Sinon si on l'ajoute!!
            self._listKey.append(cle)
            self._listValue.append(value)
        else:#Sinon on modifie la valeur!
            id=self._listKey.index(cle)
            self._listValue[id]=value
    def __delitem__(self,cle):
        """On redefinie la fonction del"""
        i=self._listKey.index(cle)
        del self._listValue[i]
        self._listKey.remove(cle)
    def __contains__(self,value):#Renvoie True si la valeur existe et False sinon
        return value in self._listKey
    def __len__(self):#On renvoie la taille des listes!!
        return len(self._listKey)
    def __str__(self):
        """On cree un dictionnaire que l'on va remplir avec 
        nos cles et valeur"""
        String=dict()
        for l in range(len(self)):
            String[self._listKey[l]]=self._listValue[l]
        return str(String)
    def sort(self):
        """Trie la liste des cles et renvoie un nouveau 'Dictionnary'"""
        liste=list()
        for i in range(len(self)):
            liste.append((self._listKey[i],self._listValue[i]))
        liste.sort()
        newDict=Dictionnary()
        for key,value in liste:
            newDict[key]=value
        return newDict
    def Keys(self):
        """On accede a la liste des cles"""
        return self._listKey
    def values(self):
        """On accede a la liste des valeurs"""
        return self._listValue
    listKey=property(Keys)
    listValue=property(values)  
    def __iter__(self):
        #Pour parcourir la liste ,on renvoie un iterateur sur la liste des cles!!
        return iter(self.listKey)
    def items(self):
        liste=list()
        for i in range(len(self)):
            liste.append((self._listKey[i],self._listValue[i]))
        return liste
    def __add__(self,newDic):
        self._listKey.extend(newDic._listKey)
        self._listValue.extend(newDic._listValue)
