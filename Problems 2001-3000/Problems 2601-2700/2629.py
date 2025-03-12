

from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count = 0
        zeroCount = 0
        for i in nums:
            if i < 0:
                count+=1
            elif i == 0:
                zeroCount+=1
            else:
                break
        return max(count,len(nums)-count-zeroCount)
    
print(Solution().maximumCount([-3,-2,-1,0,0,1,2]))
