"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        current = 1
        while True:
            if current * current == x:
                return current
            if current * current > x:
                return current-1
            current+=1

print(Solution().mySqrt(8))
