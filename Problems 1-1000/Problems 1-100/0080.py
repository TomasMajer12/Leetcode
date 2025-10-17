

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 1
        count = 1
        lastElement = nums[0]
        write_index = 0
        while i < len(nums):
            if nums[i] == lastElement:
                count+=1
            else:
                for _ in range(min(count,2)):
                    nums[write_index] = lastElement
                    write_index+=1
                lastElement = nums[i]
                count = 1
            i+=1
        for _ in range(min(count,2)):
            nums[write_index] = lastElement
            write_index+=1
        return write_index

print(Solution().removeDuplicates([1,1,1,2,2,3]))
print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))