"""
Given an integer num, return a string of its base 7 representation.
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        digits = ""
        neg = True if num > 0 else False
        num = abs(num)
        while num:
            digits= str(num % 7) + digits
            num//=7
        return digits if neg else "-"+digits

print(Solution().convertToBase7(-7))