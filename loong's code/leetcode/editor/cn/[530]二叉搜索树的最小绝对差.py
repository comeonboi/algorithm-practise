"""
<p>给你一个二叉搜索树的根节点 <code>root</code> ，返回 <strong>树中任意两不同节点值之间的最小差值</strong> 。</p>

<p>差值是一个正数，其数值等于两值之差的绝对值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg" style="width: 292px; height: 301px;" /> 
<pre>
<strong>输入：</strong>root = [4,2,6,1,3]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg" style="width: 282px; height: 301px;" /> 
<pre>
<strong>输入：</strong>root = [1,0,48,null,null,12,49]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li>树中节点的数目范围是 <code>[2, 10<sup>4</sup>]</code></li> 
 <li><code>0 &lt;= Node.val &lt;= 10<sup>5</sup></code></li> 
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与 783 <a href="https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/">https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/</a> 相同</p>

<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>广度优先搜索</li><li>二叉搜索树</li><li>二叉树</li></div></div><br><div><li>👍 462</li><li>👎 0</li></div>
"""
from cmath import inf
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = 10 ** 5 + 1
    pre = 10 ** 5 + 1
    def inOrder(self, root, res):
        if root is None:
            return
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        minRes = inf
        self.inOrder(root, res)
        for i in range(len(res) - 1):
            minRes = min(abs(res[i]-res[i+1]), minRes)
        return minRes
        # self.ans = min(self.ans, abs(root.val - self.pre))
        # # left tree
        # self.pre = root.val
        # self.getMinimumDifference(root.left)
        # self.getMinimumDifference(root.right)
        # return self.ans
# leetcode submit region end(Prohibit modification and deletion)
