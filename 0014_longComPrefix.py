
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        i = 0
        prefix = ''

        while True:
            char = ''

            for string in strs:
            
                if i >= len(string):
                    return prefix
                
                if char == '':
                    char = string[i]

                if string[i] != char:
                    return prefix
            prefix+= char 
            i+=1
            

strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))