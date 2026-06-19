class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chr = [0] * 26

        for ch in s:
            chr[ord(ch) - ord('a')] += 1

        for ch in t:
            chr[ord(ch) - ord('a')] -= 1

        for num in chr:
            if num != 0:
                return False

        return True