"""
Given two strings ransomNote and magazine, 
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rDic = {}
        mDic = {}

        for char in ransomNote:
            if char not in rDic:
                rDic[char] = 1
            else:
                rDic[char]+= 1
        
        for char in magazine:
            if char not in mDic:
                mDic[char] = 1
            else:
                mDic[char]+= 1
        
        for char in rDic.keys():
            if char not in mDic or mDic[char] < rDic[char]:
                return False
        return True

print(Solution().canConstruct(ransomNote = "aa", magazine = "ab"))