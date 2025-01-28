class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        unique_val=[]
        answer=[]
        for index1 in range(len(nums)):
            for index2 in range(index1+1,len(nums)):
                if nums[index1]==nums[index2]:
                    unique_val.append(nums[index1])
            if nums[index1] not in unique_val:
                answer.append(nums[index1])
        return answer