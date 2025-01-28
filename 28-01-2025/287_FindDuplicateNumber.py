class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums2=set()
        for value in nums:
            if value in nums2:
                return value
            else:
                nums2.add(value)
            