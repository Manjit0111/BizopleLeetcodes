class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum_area = 0
        leftPointer = 0
        rightPointer = len(height) - 1

        while leftPointer < rightPointer:
            maximum_area=max(maximum_area,(rightPointer-leftPointer)*min(height[rightPointer],height[leftPointer]))
            if height[leftPointer]<height[rightPointer]:
                leftPointer+=1
            else:
                rightPointer-=1
        return maximum_area
            