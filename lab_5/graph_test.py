import unittest
import pandas as pd
import networkx as nx
import graph_helpers


class GraphText(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.G = graph_helpers.getGraphFromFilePath(
            "data/insecta-ant-colony5-day38/insecta-ant-colony5-day38.edges")

    def test_node_count(self):
        self.assertEqual(graph_helpers.nodeCount(self.G), 66)

    def test_edge_count(self):
        self.assertEqual(graph_helpers.edgeCount(self.G), 1570)

    def test_density(self):
        self.assertEqual(round(graph_helpers.density(self.G), 6), 0.731935)

    def test_avg_degree(self):
        self.assertEqual(int(graph_helpers.averageDegree(self.G)), 47)

    def test_diameter(self):
        self.assertEqual(graph_helpers.diameter(self.G), 3)

    def test_clustering(self):
        self.assertEqual(graph_helpers.clusteringCoefficient(
            self.G), nx.clustering(self.G))

    def test_degree_dist(self):
        self.assertAlmostEqual(sum(graph_helpers.degreeDistribution(
            self.G).values()), 1)


if __name__ == "__main__":
    unittest.main()
