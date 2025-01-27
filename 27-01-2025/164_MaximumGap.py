class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_val=0
        for index1 in range(len(nums)-1):
            max_val=max(max_val,nums[index1+1]-nums[index1])
        return max_val