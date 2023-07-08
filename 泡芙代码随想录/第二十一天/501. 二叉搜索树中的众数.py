# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mapp = {}
        self.it(root, mapp)
        result_list = list(mapp.items())
        result_list.sort(key=lambda x:x[1])
        result = []
        for i in range(len(result_list)):
            if result_list[i][1]==result_list[-1][1]:
                result.append(result_list[i][0])
        return result
    def it(self,root,mapp):
        if not root:
            return mapp
        if root.val not in mapp:
            mapp[root.val] = 1
        else:
            mapp[root.val] +=1
        self.it(root.left, mapp)
        self.it(root.right, mapp)