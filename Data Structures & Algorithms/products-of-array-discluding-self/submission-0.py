class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [1] * n

        #suffix
        for i in range(1, n):
            dp[i] = nums[i-1] * dp[i-1]

        suffix = 1
        for i in range(n-1, -1, -1):
            dp[i] *= suffix
            suffix *= nums[i]


        return dp
