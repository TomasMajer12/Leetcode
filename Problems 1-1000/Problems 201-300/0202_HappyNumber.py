"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        posibilities = set()
        while True:
            digits = str(n)
            num = 0
            for i in digits:
                num+=int(i)**2
            if num == 1:
                return True
            if num in posibilities:
                return False
            posibilities.add(num)
            n = num

print(Solution().isHappy(19))
print(Solution().isHappy(2))