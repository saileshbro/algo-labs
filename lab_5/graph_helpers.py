import numpy as np
import networkx as nx
from scipy.io import mmread
import pandas as pd
import matplotlib.pyplot as plt


def nodeCount(G):
    return nx.number_of_nodes(G)


def edgeCount(G):
    return nx.number_of_edges(G)


def density(G):
    edge = edgeCount(G)
    node = nodeCount(G)
    return (2*edge)/(node*(node-1))


def degreeOfVertex(G, v):
    return len(G.adj[v])


def averageDegree(G):
    i = 0
    for V in G.nodes:
        i += degreeOfVertex(G, V)
    return i/nodeCount(G)


def diameter(G):
    return nx.diameter(G)


def clusteringCoefficient(G):
    coeffs = {}
    for V in G.nodes:
        k = len(G.adj[V])
        if(k <= 1):
            coeffs[V] = 0
            continue
        e = 0
        for v in G.adj[V]:
            for u in G.adj[V]:
                if(v == u):
                    continue
                if(G.has_edge(u, v)):
                    e += 1
        e = e/2
        coeffs[V] = (2*e)/(k*(k-1))
    return coeffs


def degreeDistribution(G):
    degreesDists = {i: 0 for i in range(len(G.nodes))}
    for i in G.nodes:
        degreesDists[degreeOfVertex(G, i)] += 1
    for i in range(len(degreesDists)):
        degreesDists[i] /= len(G.nodes)
    return degreesDists


def getGraphFromFilePath(path: str):
    if path.endswith(".edges"):
        E = pd.read_csv(path,
                        sep=" ", header=None, names=["a", "b", "w"])
        G = nx.from_pandas_edgelist(E, "a", "b", ["w"])
        return G
    else:
        a = mmread(path)
        G = nx.from_scipy_sparse_matrix(a)
        return G


def plotDegreeDistribution(G, label: str):
    a = degreeDistribution(G)
    keys = a.keys()
    values = a.values()
    plt.figure(num=label)
    plt.xlabel("$k$")
    plt.ylabel("$P(k)$")
    plt.title(label)
    plt.plot(keys, values)
