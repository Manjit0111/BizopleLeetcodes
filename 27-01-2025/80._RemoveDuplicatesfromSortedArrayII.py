class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=2
        for index in range(2,len(nums)):
            if nums[index]!=nums[k-2]:
                nums[k]=nums[index]
                k+=1
        return k