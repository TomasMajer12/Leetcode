"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) <=1:
            return s
        char_array = [char for char in s]
        i = 0
        j = len(s) -1
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        while i <= j:
            while i < len(s) and char_array[i] not in vowels:
                i+=1
            while j >= 0 and char_array[j] not in vowels:
                j-=1
       
            if i <= j and i < len(s) and j >= 0:
                char_array[i],char_array[j] = char_array[j],char_array[i]
            j-=1
            i+=1
        return ''.join(char_array)


print(Solution().reverseVowels("hello"))
print(Solution().reverseVowels("leetcode"))