class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        if len(nums)==1:
            return [nums]
        for index1 in range(len(nums)):
            value=nums[index1]
            sub_list=nums[:index1]+nums[index1+1:]
            for index2 in self.permute(sub_list):
                answer.append([value]+index2)
        return answer