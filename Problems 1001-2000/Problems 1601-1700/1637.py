"""
Given n points on a 2D plane where points[i] = [xi, yi], 
Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). 
The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.
"""

from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = 0
        xCoords = sorted([x for x,y in points])
        for i in range(len(xCoords)-1):
            ans = max(xCoords[i+1] - xCoords[i],ans)
        return ans


print(Solution().maxWidthOfVerticalArea(points = [[8,7],[9,9],[7,4],[9,7]]))