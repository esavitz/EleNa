# controller for backend
from model import MapGraph
class controller:
    def __init__(self, data):
        self.model = MapGraph([data.start, data.end])

    def get_route(self):
        pass