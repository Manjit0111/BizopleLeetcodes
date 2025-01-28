class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result=len(nums)
        for index in range(len(nums)):
            result+=index-nums[index]
        return result