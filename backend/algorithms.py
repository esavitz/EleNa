import osmnx as ox
import networkx as nx
import pandas as pd
import heapq
import json
import math

def find_all_paths(graph, start, end):
    """
        Get the list of all simple paths from the start node to the end node of the graph.
        Args:
            graph (networkX Multigraph): A networkX Multigraph
            start (int): Starting node ID in the graph
            end (int): Ending node ID in the graph
        Returns:
            list: List of all simple paths from the start node to the end node.
    """
    paths = []
    visited = set()

    def dfs(current, path):
        visited.add(current)
        if current == end:
            paths.append(path)
            return
        for neighbor in graph[current]:
            if neighbor not in visited:
                dfs(neighbor, path + [neighbor])
        visited.remove(current)

    dfs(start, [start])
    return paths

def dijkstra_max_weight(graph, start, end, max_length):
    """
        Get the list of nodes in the elevation gain maximizing path using a modified Dijkstra's algorithm.
        The method limits the length of the path to max_length.
        Args:
            graph (networkX Multigraph): A networkX Multigraph
            start (int): Starting node ID in the graph
            end (int): Ending node ID in the graph
            max_length (float): Max length of the gain maximizing path. 
        Returns:
            list: List of nodes in the elevation gain maximizing path.
    """
    distances = {node: -math.inf for node in graph}
    predecessors = {node: None for node in graph}
    visited = set()

    distances[start] = math.inf

    priority_queue = []
    heapq.heappush(priority_queue, (distances[start], start))

    while priority_queue:
        current_weight, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            break

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, attr in graph[current_node].items():
            for edge in attr.values():
                weight = edge['gain']
                max_weight = max(distances[current_node], weight)
                if max_weight > distances[neighbor]:
                    distances[neighbor] = max_weight
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (max_weight, neighbor))

        if len(predecessors) - 1 >= max_length:
            break

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()

    if path[0] != start or len(path) > max_length:
        return None  # No path found or path length exceeds the limit

    return path