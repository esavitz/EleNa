import pytest
from unittest import mock
import networkx as nx

from backend.controller import controller
from model import MapGraph

@pytest.fixture
def map_graph():
    locations = ['Amherst, MA', 'Hadley, MA']
    return MapGraph(locations)

def test_get_start_node(map_graph):
    assert isinstance(map_graph.get_start_node(), int)

def test_get_end_node(map_graph):
    assert isinstance(map_graph.get_end_node(), int)

def test_get_locations(map_graph):
    locations = map_graph.get_locations()
    assert isinstance(locations, list)
    assert len(locations) == 2
    assert isinstance(locations[0], str)
    assert isinstance(locations[1], str)

def test_set_locations(map_graph):
    new_locations = ['Chicago, USA', 'Seattle, USA']
    map_graph.set_locations(new_locations)
    assert map_graph.get_locations() == new_locations

def test_get_graph(map_graph):
    graph = map_graph.get_graph()
    assert graph is not None
    assert isinstance(graph, nx.Graph)


def test_set_shortest_path(map_graph):
    shortest_path = [1, 2, 3]
    map_graph.set_shortest_path(shortest_path)
    assert map_graph.get_shortest_path() == shortest_path

def test_set_shortest_path_length(map_graph):
    shortest_path_length = 1000.0
    map_graph.set_shortest_path_length(shortest_path_length)
    assert map_graph.get_shortest_path_length() == shortest_path_length

def test_set_shortest_path_elevation(map_graph):
    shortest_path_elevation = 200.0
    map_graph.set_shortest_path_elevation(shortest_path_elevation)
    assert map_graph.get_shortest_path_elevation() == shortest_path_elevation

def test_set_result_path(map_graph):
    result_path = [1, 2, 3, 4]
    map_graph.set_result_path(result_path)
    assert map_graph.get_result_path() == result_path

def test_set_result_path_length(map_graph):
    result_path_length = 1500.0
    map_graph.set_result_path_length(result_path_length)
    assert map_graph.get_result_path_length() == result_path_length

def test_get_result_path_length(map_graph):
    result_path_length = map_graph.get_result_path_length()
    assert result_path_length is None

def test_get_result_path_elevation(map_graph):
    result_path_elevation = map_graph.get_result_path_elevation()
    assert result_path_elevation is None

def test_set_result_path_elevation(map_graph):
    result_path_elevation = 250.0
    map_graph.set_result_path_elevation(result_path_elevation)
    assert map_graph.get_result_path_elevation() == result_path_elevation

def test_get_lat_long_route(map_graph):
    controller_obj = controller({'start': 'Amherst, MA', 'end': 'Hadley, MA'})
    with mock.patch('controller.MapGraph.get_nodes') as mock_get_nodes:
        mock_get_nodes.return_value = {
            0: {'y': 42.3750369, 'x': -72.5195706},
            1: {'y': 42.3494844, 'x': -72.5798426},
            2: {'y': 42.3653504, 'x': -72.5430027}
        }
        with mock.patch('controller.controller.ox.shortest_path') as mock_shortest_path:
            mock_shortest_path.return_value = [0, 1, 2]
            lat_long_route = controller_obj.get_lat_long_route()
            assert lat_long_route == [[42.3750369, -72.5195706], [42.3494844, -72.5798426], [42.3653504, -72.5430027]]

