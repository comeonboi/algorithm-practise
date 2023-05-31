# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        result = []
        self.recur(root,[],result)
        return result

    def recur(self,node,path,result):
        path.append(node.val)
        if not node.left and not node.right:
            result.append("->".join(map(str, path)))
        if node.left:
            self.recur(node.left, copy.copy(path), result)
        if node.right:
            self.recur(node.right, copy.copy(path), result)