"""
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

 
"""

from typing import List
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        maxCount = 1
        for i in nums:
            if i in dic:
                dic[i]+=1
                maxCount = max(maxCount,dic[i])
            else:
                dic[i]=1
        ans = []
        for i in range(maxCount):
            row = []
            for key in dic.keys():
                if dic[key] > 0:
                    row.append(key)
                    dic[key]-=1
            ans.append(row)
        return ans


print(Solution().findMatrix(nums = [1,3,4,1,2,3,1]))