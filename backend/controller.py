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
        # fig, ax = ox.plot_graph_route(self.model.get_graph(), route, node_size=0)
        #return ox.shortest_path(self.model.get_graph(), self.model.get_start_node(), self.model.get_end_node(), weight='length')
        self.model.get_shortest_path()
        if self.max == True:
            return self.model.max_elevation_path()
            #return self.model.get_shortest_path()
        else:
            return self.model.min_elevation_path()

    def get_lat_long_route(self):
        route = self.get_route()
        lat_long_route = []
        for node in route:
            lat_long_route.append([self.model.get_nodes()[node]['y'], self.model.get_nodes()[node]['x']])
        return lat_long_route