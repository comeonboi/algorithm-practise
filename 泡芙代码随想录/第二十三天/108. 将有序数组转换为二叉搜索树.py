# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.recur(nums, 0, len(nums) - 1)

    def recur(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.recur(nums, left, mid - 1)
        root.right = self.recur(nums, mid + 1, right)
        return root

