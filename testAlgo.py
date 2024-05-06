from genererMatrice import graphe
from algosCheminPlusCourt import Dijkstra
from construireChemin import construireChemin

def main():
    M = graphe(5, 0, 100)
    cheminTrouve = Dijkstra(M, 0)
    construireChemin(M, cheminTrouve)
    
main()