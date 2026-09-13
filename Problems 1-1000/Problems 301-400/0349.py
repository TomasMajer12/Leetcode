"""
Given two integer arrays nums1 and nums2, 
return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.
"""

from typing import List  # noqa: UP035


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))



print(Solution().intersection(nums1 = [1,2,2,1], nums2 = [2,2]))