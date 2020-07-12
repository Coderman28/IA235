import math as mathématiques

#fichier contenant les fonctions mathématiques nécéssaires

#la première est un formule, elle sera définie sous forme de fonctions.

def Sigmoid(x):

    return 1 / (1 + (mathématiques.e ** -x))

#AUssi une fonction, car doit trouver un maximum entre deux variables.

def ReLu(x):

    return max(0, x)

#la troisième est un dictionnaire, pour pouvoir stocker différentes variables, car c'est une focntion graphique

def Tanh(x):

    Cosh = ((mathématiques.e ** x) + (mathématiques.e ** -x)) / 2
    Sinh = ((mathématiques.e ** x) - (mathématiques.e ** -x)) / 2
    return Cosh / Sinh


