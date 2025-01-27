class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum=nums[0]
        temp_sum=nums[0]
        for value in range(1,len(nums)):
            temp_sum=max(nums[value],nums[value]+temp_sum)
            largest_sum=max(temp_sum,largest_sum)
        return largest_sum