"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""
import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        return  bin(n)[2] == "1" and bin(n).count("1") == 1

print(Solution().isPowerOfTwo(16)) 
print(Solution().isPowerOfTwo(1))
print(Solution().isPowerOfTwo(3))  