class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final_pos=len(nums)-1
        for value in range(len(nums)-2,-1,-1):
            if value+nums[value]>=final_pos:
                final_pos=value
        return final_pos==0