"""
You are given an integer array pref of size n. 
Find and return the array arr of size n that satisfies:

pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
Note that ^ denotes the bitwise-xor operation.

It can be proven that the answer is unique.
"""

from typing import List

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [0] * len(pref)
        arr[0] = pref[0] #initialize first
        for i in range(1,len(pref)):
            arr[i]=pref[i-1] ^ pref[i] #pref[i-1] ^ x == pref[i] --> x = pref[i-1] ^ pref[i]
        return arr
    
print(Solution().findArray([5,2,0,3,1]))

