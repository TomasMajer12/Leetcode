"""
For two strings s and t, we say "t divides s" if and
only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""
import re
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1),len(str2)),0,-1):
            currentDivisor = str1[:i]
            matchStr1 = re.findall(currentDivisor,str1)
            matchStr2 = re.findall(currentDivisor,str2)
            if len(str1) == i*len(matchStr1) and len(str2) == i*len(matchStr2):
                return currentDivisor
        return ""

print(Solution().gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))
print(Solution().gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))
print(Solution().gcdOfStrings(str1 = "LEET", str2 = "CODE"))