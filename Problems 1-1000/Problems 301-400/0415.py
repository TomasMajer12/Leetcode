


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []

        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry:
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0      
            total = digit1 + digit2 + carry
            carry = total // 10
            res.append(str(total % 10))
            
            i -= 1
            j -= 1
        return ''.join(res[::-1])

print(Solution().addStrings("11", "123"))  # Output: "134"
print(Solution().addStrings("456", "77"))   # Output: "533"