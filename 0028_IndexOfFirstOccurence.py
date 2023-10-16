
"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            haystack.index(needle)
        except ValueError:
            return -1
        else:
                return haystack.index(needle)


print(Solution().strStr("sadbutsad","sasd"))
                        
                        
                
        