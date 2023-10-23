
import math 
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        return False if n <= 0 else math.log(n,4) == int(math.log(n,4))

print(Solution().isPowerOfFour(4))
