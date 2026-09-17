"""
Given a string array words, 
return an array of all characters that show up in all strings within the words 
(including duplicates). You may return the answer in any order.
"""


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        intersection = set(words[0])
        for i in range(1,len(words)):
            intersection = intersection.intersection(set(words[i]))
        ret = []
        for c in intersection:
            occurance = min([word.count(c) for word in words])
            for i in range(occurance):
                ret.append(c)
        return ret

"""
Counter approach:

from collections import Counter
from functools import reduce

common = reduce(lambda a, b: a & b, map(Counter, words))
return list(common.elements())

"""

print(Solution().commonChars(["bella","label","roller"]))