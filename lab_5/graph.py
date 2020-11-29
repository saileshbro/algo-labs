import graph_helpers
import matplotlib.pyplot as plt


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
        # print("Diameter: ")
        # print(graph_helpers.diameter(self.G))
        # print()

    def plot(self, label: str):
        graph_helpers.plotDegreeDistribution(self.G, label)


if __name__ == "__main__":
    graphs = ["3elt", "176bit", "inf-power", "soc-advogato", "web-EPA"]
    for graph in graphs:
        G = GraphDetails(f"data/{graph}/{graph}.edges")
        print(graph.upper())
        print("----------------------------------")
        G.printDetails()
        G.plot(graph)
    plt.show()
