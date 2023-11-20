"""
There is an integer array nums that consists of n unique elements, but you have forgotten it. 
However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 
where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, 
either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.
"""

from typing import List
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        def create_graph(edges):
            graph = {}
            for edge in edges:
                u, v = edge
                if u not in graph:
                    graph[u] = []
                if v not in graph:
                    graph[v] = []
                graph[u].append(v)
                graph[v].append(u)
            return graph
        startNode = None
        graph = create_graph(adjacentPairs)
        for node,adj in graph.items():
            if len(adj) == 1:
                startNode = node
                break

        ans = [startNode]
        while graph[startNode]:
            node = graph[startNode].pop()
            ans.append(node)
            graph[node].remove(startNode)
            startNode = node
        return ans
      
print(Solution().restoreArray(adjacentPairs = [[2,1],[3,4],[3,2]]))