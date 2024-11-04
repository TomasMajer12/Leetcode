"""
Given a string word, compress it using the following algorithm:

Begin with an empty string comp. While word is not empty, use the following operation:
Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
Append the length of the prefix followed by c to comp.
Return the string comp.
"""

class Solution:
    def compressedString(self, word: str) -> str:
        result = ""

        count = 1
        if len(word) > 0:
            lastChar = word[0]
        for i in range(1,  len(word)):
            if count == 9:
                result=result + str(count)+lastChar
                count=1
                lastChar=word[i]                
            elif word[i] == lastChar:
                count+=1
            else:
                result=result + str(count)+lastChar
                count=1
                lastChar=word[i]
        if len(word) > 0:
            result=result + str(count)+lastChar
        return result

print(Solution().compressedString("abcdee"))
print(Solution().compressedString(""))