class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

            if count[num] > 1:
                return num

        return -1