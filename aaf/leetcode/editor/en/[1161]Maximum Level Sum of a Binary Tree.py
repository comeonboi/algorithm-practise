# Given the root of a binary tree, the level of its root is 1, the level of its 
# children is 2, and so on. 
# 
#  Return the smallest level x such that the sum of all the values of nodes at 
# level x is maximal. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
#  
# 
#  Example 2: 
# 
#  
# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  -10⁵ <= Node.val <= 10⁵ 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 24
# 46 👎 79


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        level_sum = []
        curr_nodeset = [root]

        while len(curr_nodeset):
            next_nodeset = []
            _sum = 0

            for node in curr_nodeset:
                _sum += node.val
                if node.left:
                    next_nodeset.append(node.left)
                if node.right:
                    next_nodeset.append(node.right)

            level_sum.append(_sum)
            curr_nodeset = next_nodeset

        max_sum = max(level_sum)
        ans = level_sum.index(max_sum) + 1

        return int(ans)

# leetcode submit region end(Prohibit modification and deletion)
