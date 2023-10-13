"""
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.
"""

from typing import List

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        indexOfMax = self.findMaximum(mountain_arr,0, mountain_arr.length() - 1)
        binLeft = self.binary_search(mountain_arr,0,indexOfMax,target,False)
        if  mountain_arr.get(binLeft) == target:
            return binLeft
        binRight = self.binary_search(mountain_arr,indexOfMax,mountain_arr.length() - 1,target,True)
        if mountain_arr.get(binRight) == target:
            return binRight
        return -1

    def binary_search(self, mountainArr, low,high ,target, reversed):
        while low != high:
            mid = low + (high - low) // 2
            if reversed:
                if mountainArr.get(mid) > target:
                    low = mid + 1  
                else:
                    high = mid 
            else:
                if mountainArr.get(mid) < target:
                    low = mid + 1  
                else:
                    high = mid 
        return low
    
    def findMaximum(self, mountainArr, low, high):
        while low != high:
            mid = low + (high - low) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                low = mid + 1  # Move to the right side (increasing slope).
            else:
                high = mid  # Move to the left side (decreasing slope).
        return low
    
    
print(Solution().findInMountainArray(3,[1,2,4,5,3,1]))