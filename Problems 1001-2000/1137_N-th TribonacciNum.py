"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        tribo = [0] * (n+1)
        tribo[0]= 0
        tribo[1] = tribo[2] = 1
        for i in range(3,n+1):
            tribo[i] = tribo[i-1] + tribo[i-2] + tribo[i-3]
        return tribo[n]
print(Solution().tribonacci(4))