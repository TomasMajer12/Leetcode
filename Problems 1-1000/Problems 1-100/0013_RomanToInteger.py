"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""

class Solution:
    dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    def romanToInt(self, s: str) -> int:
        ans = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and self.dic[s[i]] < self.dic[s[i+1]]:
                ans -= self.dic[s[i]]
            else:
                ans += self.dic[s[i]]
        return ans
    
print(Solution().romanToInt(s = "MCMXCIV")) #1994