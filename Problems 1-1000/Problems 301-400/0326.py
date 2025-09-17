
import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        exp = round(math.log(n,3))
        return n == 3**exp
    

print(Solution().isPowerOfThree(243))