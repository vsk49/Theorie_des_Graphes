import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def construireGraphe(M):
    G = nx.DiGraph()
    for sommets in range(1, len(M) + 1):
        G.add_node(str(sommets))
        
    for i in M:
        for j in M[i]:
            