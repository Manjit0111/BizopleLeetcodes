class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for zero in nums:
            if zero==0:
                nums.remove(zero)
                nums.append(zero)
        return nums
            