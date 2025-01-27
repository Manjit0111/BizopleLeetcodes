class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for index1 in range(len(nums)):
            for index2 in range(index1+1,len(nums)):
                if nums[index1]==nums[index2]:
                    return True
        return False