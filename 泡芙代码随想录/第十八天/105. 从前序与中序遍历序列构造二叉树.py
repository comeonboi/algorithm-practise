# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not preorder:
            return None
        return self.getHead(inorder,0,len(inorder)-1,preorder,0,len(preorder)-1)
    def getHead(self,inorder,infirst,inlast,preorder,prefirst,prelast):
        if prelast < prefirst:
            return None
        if prefirst == prelast:
            return TreeNode(preorder[prefirst])
        node = TreeNode(preorder[prefirst])
        cutindex = inorder.index(preorder[prefirst])
        node.left = self.getHead(inorder, infirst, cutindex-1, preorder, prefirst+1, prefirst+cutindex-infirst)
        node.right = self.getHead(inorder, cutindex+1, inlast, preorder, prefirst+cutindex-infirst+1, prelast)
        return node