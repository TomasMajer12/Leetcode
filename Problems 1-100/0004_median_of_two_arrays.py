
"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""


from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
    
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2

            j = (m + n + 1) // 2 - i
            
            if i < m and nums2[j-1] > nums1[i]:
                left = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                right = i - 1
            else:
                max_left = max(nums1[i-1] if i > 0 else float("-inf"), 
                            nums2[j-1] if j > 0 else float("-inf"))

                min_right = min(nums1[i] if i < m else float("inf"),nums2[j] if j < n else float("inf"))

                if (m+n) % 2 == 0:
                    return float((max_left + min_right) / 2)
                return max_left

print(Solution().findMedianSortedArrays([1,2],[3,4]))
  