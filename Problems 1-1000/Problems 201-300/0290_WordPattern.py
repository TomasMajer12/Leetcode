"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between
 a letter in pattern and a non-empty word in s.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternStorage = {}
        words = s.split()
        if len(words) != len(pattern):
            return False

        for i in range(len(words)):
            if pattern[i] not in patternStorage and words[i] not in patternStorage.values():
                patternStorage[pattern[i]] = words[i]

            if pattern[i] not in patternStorage or patternStorage[pattern[i]] != words[i]:
                return False
        return True
            

print(Solution().wordPattern(pattern = "abba", s = "dog cat cat dog"))

print(Solution().wordPattern(pattern = "abba", s = "dog cat cat fish"))

print(Solution().wordPattern(pattern = "aaaa", s = "dog cat cat dog"))
