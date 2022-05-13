import networkx as nx
import matplotlib.pyplot as plt

def create_grafo(lista):
    G = nx.Graph()
    token_list = lista
    index = 0
    for _ in range(0, len(token_list)):
        G.add_node(token_list[index][0])
        if(index != 0):
            G.add_edge(token_list[index - 1][0], token_list[index][0])
        index += 1

    nx.draw_networkx(G, with_labels = True)
    plt.show()    