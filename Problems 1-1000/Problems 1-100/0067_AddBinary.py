"""
Given two binary strings a and b, return their sum as a binary string.

"""


class Solution:
    
    def addBinary(self, a: str, b: str) -> str:
        def binToInt(bin):
            num = 0
            reverseBin = bin[::-1]
            for i in range(len(bin)):
                if reverseBin[i] == "1":
                    num+=2**i
            return num
        
        def intToBin(intNum):
            if intNum == 0:
                return "0"
            bin = ""
            while intNum > 0:
                bin= str(intNum % 2) + bin
                intNum//=2
            return bin
        
    
        return intToBin(binToInt(a) + binToInt(b))

print(Solution().addBinary("11","1"))
