"""
You are given an integer array arr.
Sort the integers in the array in ascending order by the number of 1's in their binary representation 
and in case of two or more integers have the same number of 1's you have to sort them in ascending order.
Return the array after sorting it.
"""

from typing import List
import functools
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def compare(x,y):
            if bin(x).count('1') == bin(y).count('1'): #count of '1' is same --> return ascending order
                return x - y
            return  bin(x).count('1') - bin(y).count('1') 
        return sorted(arr,key=functools.cmp_to_key(compare))
    

print(Solution().sortByBits([0,1,2,3,4,5,6,7,8]))
print(Solution().sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))
