"""
Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. 
If s[j] >= g[i], we can assign the cookie j to the child i, 
and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
"""

from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse = True)
        s.sort(reverse = True)
        res, i , j = 0 ,0,0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                res+=1
                i+=1
                j+=1
            else:
                i+=1
        return res



print(Solution().findContentChildren(g = [10,9,8,7], s = [5,6,7,8]))