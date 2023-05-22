# controller for backend
import osmnx as ox
import networkx as nx

from model import MapGraph
class controller:
    def __init__(self, data):
        self.model = MapGraph([data["start"], data["end"]])
        self.percentage = data["percentage"]
        self.max = data["max"]

    def get_route(self):
        self.model.get_shortest_path()
        if self.max == True:
            return self.model.max_elevation_path()
        else:
            return self.model.min_elevation_path()

    def get_lat_long_route(self):
        route = self.get_route()
        lat_long_route = []
        for node in route:
            lat_long_route.append([self.model.get_nodes()[node]['y'], self.model.get_nodes()[node]['x']])
        return lat_long_route