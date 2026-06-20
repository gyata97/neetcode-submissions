class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        best = 0
        maxfreq = 0

        for r, ch in enumerate(s):
            count[ch] = 1 + count.get(ch, 0)
            maxfreq = max(maxfreq, count[ch])
            while (r - l + 1) - maxfreq > k:
                count[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)

        return best