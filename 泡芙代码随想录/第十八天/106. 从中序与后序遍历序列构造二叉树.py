# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not postorder:
            return None
        return self.getHead(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

    def getHead(self, inorder, infirst, inlast, postorder, postfirst, postlast):
        print(infirst, inlast, postfirst, postlast, postorder[postlast])
        if postfirst > postlast:
            return None
        if postfirst == postlast:
            return TreeNode(postorder[postfirst])
        node = TreeNode(postorder[postlast])
        cutindex = inorder.index(postorder[postlast])
        node.left = self.getHead(inorder, infirst, cutindex - 1, postorder, postfirst,
                                 postfirst + cutindex - 1 - infirst)
        node.right = self.getHead(inorder, cutindex + 1, inlast, postorder, postfirst + cutindex - infirst,
                                  postlast - 1)
        return node
