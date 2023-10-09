"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pos = 1
        num = 0
        reversedDigits = digits[::-1]
        for i in range(len(digits)):
            num+=reversedDigits[i] * pos
            pos*=10
        num+=1
        
        return map(int, str(num))
    

print(Solution().plusOne([1,2,3]))