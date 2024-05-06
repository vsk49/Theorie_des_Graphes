import numpy.random as rd
import numpy as np

# FONCTION 

# n correspond à la taille de la matrice
# a et b avec a < b, sont des entiers correspondants à l'intervalle de la matrice
def graphe(n, a, b):
    # Génère une matrice avec 50% de 0 et 50% de 1
    M = rd.randint(0, 2, (n, n))
    # Transforme les 0 en infini et convertit la matrice en float
    M = M.astype('float64')
    
    # Remplace les coefficients 1 par des valeurs choisies aléatoirement entre a et b
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                M[i][j] = rd.randint(a, b)
            else:
                M[i][j] = np.inf

    return M

# n correspond a la taille de la matrice
# a et b avec a < b, sont des entiers correspondants à l'intervalle de la matrice
# p est la proportion variable de fleche
def graphe2(n, p, a, b): 
    # Génère une matrice avec une proportion p de flèches (1)
    M = np.random.binomial(1, p, size=(n, n)) 
    M = M.astype('float64')

    # Remplace les coefficients 1 par des valeurs choisies aléatoirement entre a et b
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                M[i][j] = np.random.randint(a, b)
            else:
                M[i][j] = np.inf
                
    return M

# EXEMPLE / TEST FONCTION
print("Graphe 1")
print(graphe(6, 1, 20))
print("\nGraphe 2")
print(graphe2(6, 0.4, 1, 20))  # Utilisation d'une proportion de 40% de flèches
