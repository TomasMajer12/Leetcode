"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myMap = {}
        for i, num in enumerate(nums):
            if num in myMap and abs(myMap[num] - i) <= k:
                    return True
            else:
                myMap[num] = i
        return False


print(Solution().containsNearbyDuplicate([99,99],2))