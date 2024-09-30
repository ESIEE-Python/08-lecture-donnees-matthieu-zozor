#### Imports et définition des variables globales
"""
importation de csv pour faciliter la lecture du fichier
"""
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """

    with open (filename,mode='r',encoding='utf8') as f:
        r = csv.reader(f,delimiter=';')
        l = list(r)
    return l

def get_list_k(data, k):
    """
    retourne la liste d'indice k de data

    Args:
        data(lst):liste de liste
        k(int):indice
    Returns:
        data[k](list): liste d'indice k
    """
    return data[k]

def get_first(l):
    """
    retourne le premier elt

    Args: 
        l(list):liste

    Returns :
        lst[0](int):entier de retour, premier
    
    """
    return l[0]

def get_last(l):
    """
    retourne le denier elt

    Args: 
        l(list):liste

    Returns :
        lst[-1](int):entier de retour, dernier
    
    """
    return l[-1]

def get_max(l):
    """
    retourne le max

    Args: 
        l(list):liste

    Returns :
        maxi(int):max de la liste
    
    """
    maxi=l[0]
    for elem in l:
        maxi=max(elem,maxi)
    return max

def get_min(l):
    """
    retourne le min

    Args: 
        l(list):liste

    Returns :
        mini(int):min de la liste
    
    """
    mini=l[0]
    for elem in l:
        mini=min(elem,mini)
    return mini

def get_sum(l):
    """
    retourne la somme des elts de l

    Args: 
        l(list):liste

    Returns :
        sum(int): la somme des entiers de la lst
    
    """
    som=0
    for elem in l:
        som+=int(elem)
    return som


#### Fonction principale


def main():
    """
    teste si la fonction lit bien les données et que les autres fonctions font ce qui est demandé
    """
    data=read_data("listes.csv")
    k=0
    l=get_list_k(data,k)
    print(l,get_first(l),get_last(l),get_max(l),get_min(l),get_sum(l))
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
