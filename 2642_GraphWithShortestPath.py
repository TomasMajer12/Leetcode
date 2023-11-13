"""
There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. 
The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] 
meaning that there is an edge from fromi to toi with the cost edgeCosti.

Implement the Graph class:

Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. 
It is guaranteed that there is no edge between the two nodes before adding this one.
int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. 
If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.
"""
from typing import List
import heapq
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.nodes = n
        self.graph = {i: {} for i in range(n)}
        for source, dest, cost in edges:
            self.graph[source][dest] = cost

    def addEdge(self, edge: List[int]) -> None:
        source, dest, cost = edge
        self.graph[source][dest] = cost

    def shortestPath(self, node1: int, node2: int) -> int:
        INF = float("inf")

        # Initialize distances with infinity for all nodes
        distances = {node: INF for node in range(self.nodes)}
        distances[node1] = 0

        # Priority queue to store (distance, node) pairs
        heap = [(0, node1)]

        while heap:
            curr_dist, curr_node = heapq.heappop(heap)
            if curr_dist > distances[curr_node]:
                continue

            for neighbor, weight in self.graph[curr_node].items():
                dist = curr_dist + weight
                if dist < distances[neighbor]:
                    distances[neighbor] = dist
                    heapq.heappush(heap, (dist, neighbor))
        return distances[node2] if distances[node2] != INF else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)