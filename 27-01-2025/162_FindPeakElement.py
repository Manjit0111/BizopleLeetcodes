class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_val=max(nums)
        index=0
        for val in range(len(nums)):
            if nums[val]==max_val:
                index=val
        return index