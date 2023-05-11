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
        self.locations = locations
        self.graph = ox.graph_from_place(locations, network_type='all')
        self.nodes = self.graph.nodes()
        self.edges = self.graph.edges()
        self.shortest_path = None
        self.shortest_path_length = None
        self.shortest_path_elevation = None
        self.result_path = None
        self.result_path_length = None
        self.result_path_elevation = None

    def get_locations(self):
        """
        Get the names of the start and end locations.

        Returns:
            list: Names of the start and end locations.
        """
        return self.locations

    def set_locations(self, locations):
        """
        Set the names of the start and end locations.

        Args:
            locations (list): Names of the start and end locations.
        """
        self.locations = locations

    def get_graph(self):
        """
        Get the networkx graph representing the street network.

        Returns:
            networkx.Graph: Graph representing the street network.
        """
        return self.graph

    def get_nodes(self):
        """
        Get the list of nodes in the graph.

        Returns:
            list: List of nodes in the graph.
        """
        return self.nodes

    def get_edges(self):
        """
        Get the list of edges in the graph.

        Returns:
            list: List of edges in the graph.
        """
        return self.edges

    def get_shortest_path(self):
        """
        Get the list of nodes in the shortest path.

        Returns:
            list: List of nodes in the shortest path.
        """
        return self.shortest_path

    def set_shortest_path(self, shortest_path):
        """
        Set the list of nodes in the shortest path.

        Args:
            shortest_path (list): List of nodes in the shortest path.
        """
        self.shortest_path = shortest_path

    def get_shortest_path_length(self):
        """
        Get the length of the shortest path in meters.

        Returns:
            float: Length of the shortest path in meters.
        """
        return self.shortest_path_length

    def set_shortest_path_length(self, shortest_path_length):
        """
        Set the length of the shortest path in meters.

        Args:
            shortest_path_length (float): Length of the shortest path in meters.
        """
        self.shortest_path_length = shortest_path_length

    def get_shortest_path_elevation(self):
        """
        Get the elevation gain of the shortest path in meters.

        Returns:
            float: Elevation gain of the shortest path in meters.
        """
        return self.shortest_path_elevation

    def set_shortest_path_elevation(self, shortest_path_elevation):
        """
        Set the elevation gain of the shortest path in meters.

        Args:
            shortest_path_elevation (float): Elevation gain of the shortest path in meters.
        """
        self.shortest_path_elevation = shortest_path_elevation

    def get_result_path(self):
        """
        Get the list of nodes in the result path as requested by the user.

        Returns:
            list: List of nodes in the result path as requested by the user.
        """
        return self.result_path

    def set_result_path(self, result_path):
        """
        Set the list of nodes in the result path as requested by the user.

        Args:
            result_path (list): List of nodes in the result path as requested by the user.
        """
        self.result_path = result_path

    def get_result_path_length(self):
        """
        Get the length of the result path in meters.

        Returns:
            float: Length of the result path in meters.
        """
        return self.result_path_length

    def set_result_path_length(self, result_path_length):
        """
        Set the length of the result path in meters.

        Args:
            result_path_length (float): Length of the result path in meters.
        """
        self.result_path_length = result_path_length

    def get_result_path_elevation(self):
        """
        Get the elevation gain of the result path in meters.

        Returns:
            float: Elevation gain of the result path in meters.
        """
        return self.result_path_elevation
    
    def set_result_path_elevation(self, result_path_elevation):
        """
        Set the elevation gain of the result path in meters.

        Args:
            result_path_elevation (float): Elevation gain of the result path in meters.
        """
        self.result_path_elevation = result_path_elevation

        

