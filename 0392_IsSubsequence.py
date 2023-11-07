"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        index = 0
        lenS = len(s)
        for i in range(len(t)):
            if  index < lenS and s[index] == t[i]:
                index+=1
            if index >= lenS:
                return True
        return index == len(t)