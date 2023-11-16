"""
Given an array of strings nums containing n unique binary strings each of length n, 
return a binary string of length n that does not appear in nums. 
If there are multiple answers, you may return any of them.
"""

from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        decNums = [int(num,base=2) for num in nums]
        decNums.sort()
        for i in range(len(decNums)):
            if decNums[i] != i :
                return bin(i)[2:].zfill(len(nums[0]))
        return bin(decNums[-1] + 1)[2:].zfill(len(nums[0]))
    
print(Solution().findDifferentBinaryString(nums = ["01","10"]))