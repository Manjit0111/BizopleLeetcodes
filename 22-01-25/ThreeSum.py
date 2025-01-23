class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer=set()
        for index in range(len(nums)-2):
            if index>0 and nums[index]==nums[index-1]:
                continue
            leftPointer=index+1
            rightPointer=len(nums)-1
            while leftPointer<rightPointer:
                total=nums[index]+nums[leftPointer]+nums[rightPointer]
                if total==0:
                    answer.add((nums[index],nums[leftPointer],nums[rightPointer]))
                    leftPointer+=1
                    rightPointer-=1
                elif total<0:
                    leftPointer+=1
                else:
                    rightPointer-=1
        return list(answer)
