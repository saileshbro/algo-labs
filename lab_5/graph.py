import graph_helpers
import matplotlib.pyplot as plt
import networkx as nx


class GraphDetails():
    def __init__(self, path: str):
        self.G = graph_helpers.getGraphFromFilePath(path)

    def printDetails(self):
        print("NodeCount: ")
        print(graph_helpers.nodeCount(self.G))
        print()
        print("EdgeCount: ")
        print(graph_helpers.edgeCount(self.G))
        print()
        print("Density: ")
        print(graph_helpers.density(self.G))
        print()
        print("AverageDegree: ")
        print(graph_helpers.averageDegree(self.G))
        print()
        print("Diameter: ")
        print(graph_helpers.diameter(self.G))
        print()
        print("Clustering Coefficient: ")
        print(graph_helpers.clusteringCoefficient(self.G))
        print()

    def plot(self, label: str):
        graph_helpers.plotDegreeDistribution(self.G, label)

    def drawGraph(self):
        nx.draw(self.G)
        plt.show()


if __name__ == "__main__":
    G = GraphDetails(
        "data/insecta-ant-colony5-day38/insecta-ant-colony5-day38.edges")
    print("insecta-ant-colony5-day38".upper())
    print("----------------------------------")
    G.printDetails()
    G.drawGraph()
    plt.show()
