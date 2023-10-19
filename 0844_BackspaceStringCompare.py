"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def remove_backspace(string):
            stack = []
            for i in string:
                if i == '#' and stack:
                    stack.pop()
                elif i != '#':
                    stack.append(i)
            return stack

          
        return remove_backspace(s) == remove_backspace(t)
    
print(Solution().backspaceCompare("ab#c","ad#c"))
print(Solution().backspaceCompare("ab##","c#d#"))
print(Solution().backspaceCompare("a#c","b"))