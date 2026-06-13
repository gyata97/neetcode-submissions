class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dp = set()

        for num in nums:
            if num in dp:
                return True
            dp.add(num) 

        return False