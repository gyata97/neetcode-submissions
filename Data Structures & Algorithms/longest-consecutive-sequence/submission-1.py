class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        best = 0

        for num in nums:
            seen.add(num)

        for num in nums:
            if num - 1 not in seen:
                cur = num
                count = 0
                while cur in seen:
                    count += 1
                    cur += 1
                best = max(best, count)

        return best
