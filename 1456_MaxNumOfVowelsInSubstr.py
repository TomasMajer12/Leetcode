"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        maxCount = 0
        for i in range(k):
            if s[i] in vowels:
                maxCount+=1
        currentCount = maxCount
        for i in range(1,len(s)-k+1):
            if s[i-1] in vowels:
                currentCount-=1
            
            if s[i+k-1] in vowels:
                currentCount+=1
            maxCount = max(currentCount,maxCount)
        return maxCount
        

print(Solution().maxVowels(s = "abciiidef", k = 3))
print(Solution().maxVowels(s = "weallloveyou", k = 7))