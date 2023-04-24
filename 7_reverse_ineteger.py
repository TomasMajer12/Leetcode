"""
Given a signed 32-bit integer x, return x with its digits reversed.
 If reversing x causes the value to go outside the signed 
 32-bit integer range [-2**31, 2**31 - 1], then return 0.
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            rev = int(str(x)[::-1])
            if rev > 2**31:
                return 0
            return rev
        else:
            rev = int("-"+str(str(x)[1:])[::-1])
            if rev < -2**31:
                return 0
            return rev



print(Solution().reverse(123))
print(Solution().reverse(-123))
