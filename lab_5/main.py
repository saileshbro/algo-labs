from graph import GraphDetails
import matplotlib.pyplot as plt
if __name__ == "__main__":
    graphs = ["3elt", "176bit", "inf-power", "soc-advogato", "web-EPA"]
    for graph in graphs:
        G = GraphDetails(f"data/{graph}/{graph}.edges")
        print(graph.upper())
        print("----------------------------------")
        G.printDetails()
        G.plot(graph)
    plt.show()
