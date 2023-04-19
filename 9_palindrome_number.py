
"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False
    
print(Solution().isPalindrome(x=123321))