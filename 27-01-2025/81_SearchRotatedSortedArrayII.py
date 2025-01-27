class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for index1 in range(len(nums)):
            if nums[index1]==target:
                return True
        return False    