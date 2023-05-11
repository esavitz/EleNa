import osmnx as ox
import networkx as nx

class MapGraph:
    def __init__(self, location):
        """
        Initialize a MapGraph object.

        Args:
            location (str): Name of the location to retrieve the graph for.

        Attributes:
            location (str): Name of the location.
            graph (networkx.Graph): Networkx graph representing the street network.
            nodes (list): List of nodes in the graph.
            edges (list): List of edges in the graph.
            shortest_path (list): List of nodes in the shortest path.
            result_path (list): List of nodes in the result path as requested by the user.
        """
        self.location = location
        self.graph = ox.graph_from_place(location, network_type='all')
        self.nodes = self.graph.nodes()
        self.edges = self.graph.edges()
        self.shortest_path = None
        self.result_path = None
