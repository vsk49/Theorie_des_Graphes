import numpy.random as rd
import numpy as np

# FONCTION 

# n correspond à la taille de la matrice
# a et b avec a < b, sont des entiers correspondants à l'intervalle de la matrice
def graphe(n, a, b):
    # Génère une matrice avec 50% de 0 et 50% de 1
    M = rd.choice([0, 1], size=(n, n), p=[0.5, 0.5])

    # Remplace les coefficients 1 par des valeurs choisies aléatoirement entre a et b
    for i in range(n):
        for y in range(n):
            if M[i][y] == 1:
                M[i][y] = rd.randint(a, b)

    # Transforme les 0 en infini et convertit la matrice en float
    M = M.astype('float64')
    M[M == 0] = np.inf

    return M


# n correspond a la taille de la matrice
# a et b avec a < b, sont des entiers correspondants à l'intervalle de la matrice
# p est la proportion variable de fleche
def graphe2(n, p, a, b):
  M = np.random.binomial(1, p, size=(n, n))  # Génère une matrice avec une proportion p de flèches (1)

  # Remplace les coefficients 1 par des valeurs choisies aléatoirement entre a et b
  for i in range(n):
      for j in range(n):
          if M[i][j] == 1:
              M[i][j] = np.random.randint(a, b)
  # Transforme les 0 en infini et convertis la matrice en float
  M = M.astype('float64')
  M[M == 0] = np.inf
  return M

# EXEMPLE / TEST FONCTION
print("Graphe 1")
print(graphe(6, 1, 20))
print("\nGraphe 2")
print(graphe2(6, 0.4, 1, 20))  # Utilisation d'une proportion de 40% de flèches
