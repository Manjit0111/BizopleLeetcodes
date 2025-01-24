class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num=[no1 for no1 in nums if no1>0]
        num.sort()
        target=1
        for no2 in num:
            if no2==target:
                target+=1
            elif no2>target:
                return target
        return target 
        