import fonctions
import connections

#ce fichier est le code principale

NA = float(input("Quel est la première valeur ? : "))
NB = float(input("Quel est la deuxième valeur ? : "))

NC = fonctions.Sigmoid((NA * connections.ac) + (NB * connections.bc))
ND = fonctions.Sigmoid((NA * connections.ad) + (NB * connections.bd))
NE = fonctions.Sigmoid((NA * connections.ae) + (NB * connections.be))

#NF = fonctions.Tanh(NC * connections.cf + ND * connections.df + NE * connections.ef)
NF = fonctions.Sigmoid((NC * connections.cf) + (ND * connections.df) + (NE * connections.ef))

print("le résultat est : ", NF)

