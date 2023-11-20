"""
You are given an integer n and an integer start.

Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
"""



class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = start
        curr = start
        for _ in range(n-1):
            curr+=2
            xor^=curr
        return xor

print(Solution().xorOperation(4,3))
print(Solution().xorOperation(5,0))