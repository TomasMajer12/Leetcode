"""
You are given an integer array target and an integer n.

You have an empty stack with the two following operations:

"Push": pushes an integer to the top of the stack.
"Pop": removes the integer on the top of the stack.
You also have a stream of the integers in the range [1, n].

Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target. 
You should follow the following rules:

If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.
If the stack is not empty, pop the integer at the top of the stack.
If, at any moment, the elements in the stack (from the bottom to the top) are equal to target, do not read new integers from the stream and do not do more operations on the stack.
Return the stack operations needed to build target following the mentioned rules. If there are multiple valid answers, return any of them.

"""
from typing import List
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        sol = []

        #if the target doesnt start if 1, we need to Push and Pop the numbers from [1:n]
        if target[0] != 1:
            for i in range(target[0]-1):
                sol.append("Push")
                sol.append("Pop")  

        sol.append("Push")
        for i in range(len(target)-1):

            if target[i+1] - target[i] == 1:
                sol.append("Push")
            else:
                for j in range(1,target[i+1] - target[i]):
                    sol.append("Push")
                    sol.append("Pop")
                sol.append("Push")
        
        return sol

print(Solution().buildArray([2,3,4],4))
