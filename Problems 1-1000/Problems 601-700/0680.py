"""
Given a string s, return true if the s can be palindrome 
after deleting at most one character from it.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s)-1
        while i < j:
            if s[i] == s[j]:
                i+=1
                j-=1
            elif s[i+1] == s[j] or s[i] == s[j-1]:
                new_str1 = s[i+1:j+1]
                new_str2 = s[i:j]
                return new_str1 == new_str1[::-1] or new_str2 == new_str2[::-1]
            else:
                return False
        return True


print(Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
