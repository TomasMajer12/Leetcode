"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ""
        for i in range(min(len(word1),len(word2))):
            out+=word1[i]
            out+=word2[i]
        
        if len(word1) > len(word2):
            out+=word1[len(word2):]
        elif len(word1) < len(word2):
            out+=word2[len(word1):]
        return out

print(Solution().mergeAlternately(word1 = "abc", word2 = "pqr"))
print(Solution().mergeAlternately(word1 = "ab", word2 = "pqrs"))
print(Solution().mergeAlternately(word1 = "abcd", word2 = "pq"))