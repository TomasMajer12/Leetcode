"""
A phrase is a palindrome if, after converting all uppercase 
letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s:
            if char.isalnum():
                newStr+=char.lower()
        return newStr[::-1] == newStr

print(Solution().isPalindrome(s = "A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("0P"))