


class Solution:
    def addDigits(self, num: int) -> int:
        
        while len(str(num)) > 1:
            count = 0
            for digit in str(num):
                count+=int(digit)
            num = count
        return num
    
print(Solution().addDigits(38))