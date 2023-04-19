from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @return int整型一维数组
#
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []

        # write code here
        def bfs(node, visited: list):
            if not node:
                return
            visited.append(node.val)
            bfs(node.left, visited)
            bfs(node.right, visited)
            return
        bfs(root, lst)
        return lst
