class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer=[]
        if len(nums)==1 and target in nums:
            return [0,0]
        if target not in nums:
            return [-1,-1]
        for index in range(len(nums)):
            if nums[index]==target:
                answer.append(index)
        return [answer[0],answer[-1]]
                