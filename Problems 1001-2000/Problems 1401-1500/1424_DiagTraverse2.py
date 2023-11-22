"""
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.
"""



from typing import List
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        rows = [0]
        ans = []
        d = 0
        while rows:
            nxt = []
            if d < len(nums) - 1:
                nxt.append(rows[0] + 1)
            for i in rows:
                j = d - i
                ans.append(nums[i][j])
                if len(nums[i]) > j + 1:
                    nxt.append(i)
            rows = nxt
            d += 1
        return ans
print(Solution().findDiagonalOrder(nums = [[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().findDiagonalOrder(nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))
print(Solution().findDiagonalOrder(nums = [[1,2,3,4,5,6]]))
print(Solution().findDiagonalOrder(nums = [[6],[8],[6,1,6,16]]))
print(Solution().findDiagonalOrder(nums = [[20,17,13,14],[12,6],[3,4]]))
