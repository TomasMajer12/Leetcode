"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a 
direct path going from cityAi to cityBi. 
Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
"""

from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        myMap = {}

        for path in paths:
            myMap[path[0]] = 1
            if path[1] not in myMap:
                myMap[path[1]] = 0
        
        for city in myMap.items():
            if city[1] == 0:
                return city[0]


print(Solution().destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))