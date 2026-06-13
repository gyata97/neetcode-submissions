class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ch = [0] * 26

        for letter in s:
            ch[ord(letter) - ord('a')] += 1

        for letter in t:
            ch[ord(letter) - ord('a')] -= 1

        for num in ch:
            if num != 0:
                return False

        return True