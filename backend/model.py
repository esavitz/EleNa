import osmnx as ox
import networkx as nx
import pandas as pd
import json
from pandas import json_normalize
import requests as req
from algorithms import find_all_paths, dijkstra_max_weight

class MapGraph:
    def __init__(self, locations):
        """
        Initialize a MapGraph object.

        Args:
            locations (list): Names of the start and end locations to retrieve the graph for.

        Attributes:
            locations (list): Names of the start and end locations.
            graph (networkx.Graph): Networkx graph representing the street network.
            start_geo (tuple): Tuple of the start location's latitude and longitude.
            end_geo (tuple): Tuple of the end location's latitude and longitude.
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

        # Create the graph from locations
        self.graph = ox.graph_from_place(locations, network_type='all', buffer_dist=2000)

        # Add elevation to the graph
        self.graph = ox.elevation.add_node_elevations_google(self.graph, api_key='AIzaSyA8gjr4DmvMClK0_k4J1wl_PNd3ljYoj2k')
        self.graph = ox.elevation.add_edge_grades(self.graph)

        edge_attributes = ox.graph_to_gdfs(self.graph, nodes=False).columns
        #print(edge_attributes)

        self.start_geo = ox.geocode(locations[0])
        self.end_geo = ox.geocode(locations[1])
        self.nodes = self.graph.nodes()
        self.edges = self.graph.edges()
        self.shortest_path = None
        self.shortest_path_length = None
        self.shortest_path_elevation = None
        self.result_path = None
        self.result_path_length = None
        self.result_path_elevation = None

    def get_start_node(self):
        """
        Get the start node.

        Returns:
            int: Start node ID.
        """
        return ox.distance.nearest_nodes(self.graph, self.start_geo[1], self.start_geo[0])

    def get_end_node(self):
        """
        Get the end node.

        Returns:
            int: End node ID.
        """
        return ox.distance.nearest_nodes(self.graph, self.end_geo[1], self.end_geo[0])

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
        self.shortest_path = ox.shortest_path(self.get_graph(), self.get_start_node(), self.get_end_node(), weight='length')

        self.shortest_path_length = int(sum(ox.utils_graph.get_route_edge_attributes(self.get_graph(), self.shortest_path, "length")))

        #print("shortest path: ", self.shortest_path)
        self.shortest_path_elevation = self.get_elevation_gain(self.shortest_path)
        
        print(f"shortest path length: {self.shortest_path_length}")
        print(f"elevation gain: {self.shortest_path_elevation}")
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

    def get_elevation_gain(self, path):
        """
        Returns the elevation gain of a path in meters.

        Args:
            path (float): Path consisting of a list of nodes
        """
        if len(path) == 0 or path == None:
            return None
        gain = 0
        for i in range(len(path)-1):
            diff = self.graph.nodes[path[i+1]]['elevation'] - self.graph.nodes[path[i]]['elevation']
            if diff > 0:
                gain += diff
        return gain
    
    def get_elevation_loss(self, path):
        """
        Returns the elevation gain of a path in meters.

        Args:
            path (float): Path consisting of a list of nodes
        """
        if len(path) == 0 or path == None:
            return None
        loss = 0
        for i in range(len(path)-1):
            diff = self.graph.nodes[path[i+1]]['elevation'] - self.graph.nodes[path[i]]['elevation']
            if diff < 0:
                loss += abs(diff)
        return loss


    def min_elevation_path(self):
        """
        Get the list of nodes in the elevation gain minimizing path.

        Returns:
            list: List of nodes in theelevation gain minimizing path.
        """
        
        for u, v, key in self.graph.edges(keys=True):
            edge = []
            edge.append(u)
            edge.append(v)
            self.graph[u][v][key]['gain'] = self.get_elevation_gain(edge)

        self.result_path = ox.shortest_path(self.get_graph(), self.get_start_node(), self.get_end_node(), weight='gain')
        self.result_path_length = int(sum(ox.utils_graph.get_route_edge_attributes(self.get_graph(), self.result_path, "length")))
        self.result_path_elevation = self.get_elevation_gain(self.result_path)
        
        print(f"min gain path length: {self.result_path_length}")
        print(f"min gain elevation gain: {self.result_path_elevation}")
        return self.result_path_elevation
    
    def max_elevation_path_bruteforce(self, max_length_mult=2.0):
        """
        Get the list of nodes in the elevation gain maximizing path using a bruteforce solution.

        Returns:
            list: List of nodes in the elevation gain maximizing path.
        """

        for u, v, key in self.graph.edges(keys=True):
            edge = []
            edge.append(u)
            edge.append(v)
            self.graph[u][v][key]['gain'] = self.get_elevation_gain(edge)

        paths = find_all_paths(self.graph, self.get_start_node(), self.get_end_node())

        path_el = {}
   
        for path in paths:
            path_el[path] = self.get_elevation_gain(path)

        sorted_path_el = dict(sorted(path_el.items(), reverse=True))

        for key in sorted_path_el.keys():
            path_length = int(sum(ox.utils_graph.get_route_edge_attributes(self.get_graph(), key, "length")))
            if path_length <= max_length_mult*self.shortest_path_length:
                print(f"max gain path length: {path_length}")
                print(f"max elevation path gain: {sorted_path_el[key]}")
                self.result_path = key
                self.result_path_length = path_length
                self.result_path_elevation = sorted_path_el[key]
                return self.result_path 
        return None
    
    def max_elevation_path(self, max_length_mult=2.0):
        """
        Get the list of nodes in the elevation gain maximizing path using a modified Dijkstra's algorithm.
        If no maximizing path is found, the method returns the shortest path.

        Returns:
            list: List of nodes in the elevation gain maximizing path.
        """

        for u, v, key in self.graph.edges(keys=True):
            edge = []
            edge.append(u)
            edge.append(v)
            self.graph[u][v][key]['gain'] = self.get_elevation_gain(edge)

        max_length = self.shortest_path_length*max_length_mult
        self.result_path = dijkstra_max_weight(self.graph, self.get_start_node(), self.get_end_node(), max_length)
        if self.result_path == None:
            self.result_path = self.shortest_path
        self.result_path_length = int(sum(ox.utils_graph.get_route_edge_attributes(self.get_graph(), self.result_path, "length")))
        self.result_path_elevation = self.get_elevation_gain(self.result_path)
        
        print(f"max gain path length: {self.result_path_length}")
        print(f"max gain elevation gain: {self.result_path_elevation}")

        return self.result_path





