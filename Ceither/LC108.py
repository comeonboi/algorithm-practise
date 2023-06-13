# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(head, tail):
            if head > tail:
                return None
            mid = (head + tail) // 2
            root = TreeNode(nums[mid])
            root.left = build_tree(head, mid - 1)
            root.right = build_tree(mid + 1, tail)
            return root
        return build_tree(0, len(nums) - 1)