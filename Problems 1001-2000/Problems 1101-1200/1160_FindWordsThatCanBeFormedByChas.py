"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words
"""

from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans=0
        for word in words:
            for char in word:
                if chars.count(char) < word.count(char):
                    break
            else:
                ans+=len(word)
        return ans


print(Solution().countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
