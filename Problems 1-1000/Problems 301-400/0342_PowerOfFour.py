"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""
import math 
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        return False if n <= 0 else math.log(n,4) == int(math.log(n,4))

print(Solution().isPowerOfFour(4))
