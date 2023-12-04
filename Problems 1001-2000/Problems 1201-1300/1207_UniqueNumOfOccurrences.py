"""
Given an array of integers arr, return true if the number of 
occurrences of each value in the array is unique or false otherwise.
"""

from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}

        for num in arr:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num]+=1
        return sorted(list(dic.values())) == sorted(list(set(dic.values())))
    

print(Solution().uniqueOccurrences(arr = [1,2,2,1,1,3]))