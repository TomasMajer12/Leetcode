"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.
 
"""



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(str.split(s)[-1])        
    

print(Solution().lengthOfLastWord(" fly me   to   the moon      "))