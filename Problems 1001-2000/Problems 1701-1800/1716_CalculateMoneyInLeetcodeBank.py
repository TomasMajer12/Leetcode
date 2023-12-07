"""
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, 
he will put in $1 more than the day before. On every subsequent Monday, 
he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
"""

class Solution:
    def totalMoney(self, n: int) -> int:
        k = n // 7
        ans = 0
        for i in range(1,k+1):
            ans+=7*i + 21 
        if n % 7 != 0:
            for i in range(k+1,k+1+n%7):
                ans+=i
        return ans


print(Solution().totalMoney(10))