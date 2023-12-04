"""
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.
"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""

        for i in range(len(num)-2):
            isGood = True
            for j in range(2):
                if num[i+j] != num[i+j+1]:
                    isGood = False
            if isGood:
                if ans == "":
                    ans = num[i:(i+3)]
                elif int(ans[0]) < int(num[i]):
                    ans = num[i:(i+3)]
        return ans

print(Solution().largestGoodInteger("4564842777999"))