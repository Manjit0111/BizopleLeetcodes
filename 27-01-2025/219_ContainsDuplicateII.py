class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for index1 in range(len(nums)):
            for index2 in range(index1+1,len(nums)):
                if nums[index1]==nums[index2] and abs(index1 - index2) <= k:
                    return True
        return False