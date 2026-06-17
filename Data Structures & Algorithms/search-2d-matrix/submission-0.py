class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = left + ((right - left)//2)
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return False

        for nums in matrix:
            if binarySearch(nums):
                return True

        return False