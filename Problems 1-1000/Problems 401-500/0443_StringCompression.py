"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, 
be stored in the input character array chars. Note that group lengths 
that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

"""
from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        currentChar = chars[0]
        count = 1
        for i in range(1,len(chars)):
            if chars[i] == currentChar:
                count+=1
            else:
                chars[index] = currentChar
                index+=1
                if count > 1:
                    for char in str(count):
                        chars[index] = char
                        index+=1
                currentChar=chars[i]
                count=1
        chars[index] = currentChar
        index+=1
        if count > 1:
            for char in str(count):
                chars[index] = char
                index+=1
        return index 
    
print(Solution().compress( chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
