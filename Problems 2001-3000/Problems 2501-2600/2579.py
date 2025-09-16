


class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 4 * n * (n-1) // 2

print(Solution().coloredCells(1))
print(Solution().coloredCells(2))
print(Solution().coloredCells(3))