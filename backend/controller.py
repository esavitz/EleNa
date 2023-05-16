# controller for backend
import osmnx as ox
import networkx as nx

from model import MapGraph
class controller:
    def __init__(self, data):
        self.model = MapGraph([data.start, data.end])

    def get_route(self):
        route = ox.shortest_path(self.model.get_graph(), self.model.get_locations()[0], self.model.get_locations()[1], weight='length')
        return route