"""
You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of times:

Choose two elements with equal values and delete them from the array.
Choose three elements with equal values and delete them from the array.
Return the minimum number of operations required to make the array empty, or -1 if it is not possible.
"""
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        countingSort = {}

        for num in nums:
            if num in countingSort:
                countingSort[num]+=1
            else:
                countingSort[num]=1
        ans = 0

        for i in countingSort.values():
            if i==1:
                return -1
            ans+=(i+2)//3

        return ans

print(Solution().minOperations(nums = [2,3,3,2,2,4,2,3,4]))
print(Solution().minOperations(nums = [2,1,2,2,3,3]))