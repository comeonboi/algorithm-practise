from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果找到了一个数，但是没有找到另一个数，就直接说明他们不在同一个子树中
        if not root or root == p or root == q:
            return root
        # 递归左子树
        left = self.lowestCommonAncestor(root.left, p, q)
        # 递归右子树
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果左子树和右子树都不为空，说明p和q分别在左右子树中，那么当前节点就是他们的公共祖先
        if left and right:
            return root
        # 如果左子树为空，说明p和q都在右子树中，那么右子树的公共祖先就是他们的公共祖先
        if not left:
            return right
        # 如果右子树为空，说明p和q都在左子树中，那么左子树的公共祖先就是他们的公共祖先
        if not right:
            return left


