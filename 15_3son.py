

from typing import List
import itertools

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        allperms = itertools.permutations(nums,3)
        allgoals = []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    list3 = [nums[i],nums[j],nums[k]]
                    if sum(list3) == 0 and sorted(list3) not in allgoals:
                        allgoals.append(sorted(list3))

        return allgoals
    

print(Solution().threeSum([-1,0,1,2,-1,-4]))

