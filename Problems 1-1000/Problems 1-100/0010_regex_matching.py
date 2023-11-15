"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
"""

import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        x = re.search(p,s)
        if x == None:
            return False
        if x.span()[0] == 0 and x.span()[1] == len(s):
            return True
        return False
    
print(Solution().isMatch("aaaa","a*"))