

"""
Given a string s, find the length of the longest 
substring
 without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlenght = 0
        seen = {}
        start = 0
        for i in range(len(s)):
            if s[i] in seen:
                start = max(start, seen[s[i]] + 1)
            seen[s[i]] = i
            maxlenght = max(maxlenght,i-start+1)
        
        return maxlenght
    

print(Solution().lengthOfLongestSubstring("pwwkew"))