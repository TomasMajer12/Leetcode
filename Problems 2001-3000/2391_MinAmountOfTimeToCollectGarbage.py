"""
You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. 
garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. 
Picking up one unit of any type of garbage takes 1 minute.

You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.

There are three garbage trucks in the city, each responsible for picking up one type of garbage. 
Each garbage truck starts at house 0 and must visit each house in order; 
however, they do not need to visit every house.

Only one garbage truck may be used at any given moment. 
While one truck is driving or picking up garbage, the other two trucks cannot do anything.

Return the minimum number of minutes needed to pick up all the garbage.
"""
from typing import List
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        def getCount(garbageType,travel,garbage):
            time = 0
            skip = 0
            for i in range(len(travel) + 1):
                if i == 0:
                    time+= garbage[i].count(garbageType)
                elif garbageType in garbage[i]:
                    time+= garbage[i].count(garbageType) + travel[i-1] + skip
                    skip=0
                else:
                    skip+=travel[i-1]
            return time
        return getCount("G",travel,garbage) + getCount("P",travel,garbage) + getCount("M",travel,garbage)          
        

print(Solution().garbageCollection(garbage = ["G","P","GP","GG"], travel = [2,4,3]))
print(Solution().garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10]))