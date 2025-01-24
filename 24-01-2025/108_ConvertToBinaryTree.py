# Definition for a binary tree node.
# class TreeNode:
    # def __init__(self, val=0, left=None, right=None):
    #     self.val = val
    #     self.left = left
    #     self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bstConversion(left,right):
            if left>right:
                return None
            mid_val=(left+right)//2
            left=bstConversion(left,mid_val-1)
            right=bstConversion(mid_val+1,right)
            return TreeNode(nums[mid_val],left,right)
        return bstConversion(0,len(nums)-1)