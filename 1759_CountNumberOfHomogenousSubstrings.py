"""
Given a string s, return the number of homogenous substrings of s. 
Since the answer may be too large, return it modulo 109 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.
"""


class Solution:
    def countHomogenous(self, s: str) -> int:
        char = s[0]
        count = lenght = 0
        for i in range(len(s)):
            if s[i] == char:
                lenght+=1
            else:
                char = s[i]
                count+=(lenght*(lenght+1) // 2) # n + n-1 + n-2 + .... + 1 
                lenght=1
        count+=(lenght*(lenght+1) // 2)
        return count % (10**9 + 7)
print(Solution().countHomogenous("abbcccaa"))
print(Solution().countHomogenous("xy"))
print(Solution().countHomogenous("zzzzz"))
