

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        maxlen = 0
        maxString = ""
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                if j-i < maxlen: #not longest
                    continue
                substring = s[i:j]
                if substring == substring[::-1] and len(substring) > maxlen: #is palindrom and longest
                    maxlen = len(substring)
                    maxString = substring

        return maxString

