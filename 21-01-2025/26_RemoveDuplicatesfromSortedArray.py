class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer=0
        for index in range(1,len(nums)):
            if nums[index]!=nums[pointer]:
                pointer+=1
                nums[pointer]=nums[index]
        return pointer+1