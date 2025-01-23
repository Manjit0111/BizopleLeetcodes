class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for index in range(len(nums) - 2):  
            leftPointer, rightPointer = index + 1, len(nums) - 1  

            while leftPointer < rightPointer:
                current_sum = nums[index] + nums[leftPointer] + nums[rightPointer]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    leftPointer += 1
                elif current_sum > target:
                    rightPointer -= 1 
                else:
                    return current_sum 

        return closest_sum  
                    
