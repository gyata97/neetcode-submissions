class Solution:
    def isPalindrome(self, s: str) -> bool:
        nstr = ''

        for chr in s:
            if chr.isalnum():
                nstr += chr.lower()

        return nstr == nstr[::-1]