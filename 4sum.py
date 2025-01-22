class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answer=[]
        for index1 in range(len(nums)):
            for index2 in range(index1+1,len(nums)):
                for index3 in range(index2+1,len(nums)):
                    for index4 in range(index3+1,len(nums)):
                        if nums[index1]+nums[index2]+nums[index3]+nums[index4]==target:
                            list1=nums[index1],nums[index2],nums[index3],nums[index4]
                            if list1 not in answer:
                                answer.append(list1)
        return answer