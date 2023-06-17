# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return nums
        root = self.getHead(nums,0,len(nums)-1)
        return root
    def getHead(self,nums,start,end):
        if start > end:
            return None
        if start==end:
            return TreeNode(nums[start])
        cutpoint = nums.index(max(nums[start:end+1]))
        node = TreeNode(nums[cutpoint])
        node.left = self.getHead(nums, start, cutpoint-1)
        node.right = self.getHead(nums, cutpoint+1, end)
        return node