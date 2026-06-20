class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mp = {}

        for num in nums:
            mp[num] = 1 + mp.get(num, 0)

        for num in mp:
            if mp.get(num, 0) == 1:
                return num

        return -1