
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for c in s:
        
            if c == '(':
                stack.append(')')
            
            elif c == '{':
                stack.append('}')
         
            elif c == '[':
                stack.append(']')
       
            elif c in ['}',')',']']:
                if len(stack) == 0:
                    return False
                if stack.pop() == c:
                    continue
                else:
                    return False

        if len(stack) == 0:
            return True
        return False

print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))