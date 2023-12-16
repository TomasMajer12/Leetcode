class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, start, end):
        self.adj_matrix[start][end] = 1

    def get_adj_matrix(self):
        return self.adj_matrix

def min_cost_assignment(graph, costs):
    num_vertices = len(graph)
    len_costs = len(costs)
    dp = [[float('inf')] * len(costs) for _ in range(num_vertices)] 

    for j in range(len(costs)):
        dp[0][j] = costs[j]

    for i in range(1,num_vertices):
        for j in range(len_costs):
            for k in range(len_costs):
                if graph[i][k] != 1 :
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + costs[j])
    print(dp)
    return min(dp[-1])

costs = [25, 4, 18, 3]
employees = [[1,2,3,4,-1],[4,4,4,4,-1],[4,4,3,4,-1],[4,4,3,4,-1,3,3]]




for e in employees:
    graph = Graph(len(e))
    arr = []
    for i in range(len(e)):
        if e[i] != -1:
            graph.add_edge(i,e[i])
        # else:
        #     arr.append(i)
        # for a in arr:
        #     adj = graph.get_adj_matrix()
        #     for k in range(len(e)):
        #         if adj[k][a] == 1:
        #             graph.add_edge(a,k)

    print(graph.get_adj_matrix())

    print("Min cost:", min_cost_assignment(graph.get_adj_matrix(), costs))

import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,5)
G.add_edge(4,6)
G.add_edge(1,6)
G.add_edge(2,6)
G.add_edge(7,8)
G.add_edge(9,8)

tree = nx.bfs_tree(G, 4)
nx.draw(tree)
plt.savefig('bfs_image.png')