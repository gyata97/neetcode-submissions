class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmp = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hmp:
                return sorted([i, hmp[diff]])
            
            hmp[nums[i]] = i

        
        return [-1,-1]