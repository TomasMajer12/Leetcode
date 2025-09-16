

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        prev1 = 3
        prev2 = 2
        curr = 0
        for i in range(3,n):
            curr = prev1 + prev2
            prev1,prev2 = curr,prev1
        return curr
print(Solution().climbStairs(5))