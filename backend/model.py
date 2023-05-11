import osmnx as ox
import networkx as nx

class MapGraph:
    def __init__(self, locations):
        """
        Initialize a MapGraph object.

        Args:
            locations (list): Names of the start and end locations to retrieve the graph for.

        Attributes:
            locations (list): Names of the start and end locations.
            graph (networkx.Graph): Networkx graph representing the street network.
            nodes (list): List of nodes in the graph.
            edges (list): List of edges in the graph.
            shortest_path (list): List of nodes in the shortest path.
            shortest_path_length (float): Length of the shortest path in meters.
            shortest_path_elevation (float): Elevation gain of the shortest path in meters.
            result_path (list): List of nodes in the result path as requested by the user.
            result_path_length (float): Length of the result path in meters.
            result_path_elevation (float): Elevation gain of the result path in meters.
        """
        self.location = locations
        self.graph = ox.graph_from_place(locations, network_type='all')
        self.nodes = self.graph.nodes()
        self.edges = self.graph.edges()
        self.shortest_path = None
        self.shortest_path_length = None
        self.shortest_path_elevation = None
        self.result_path = None
        self.result_path_length = None
        self.result_path_elevation = None
