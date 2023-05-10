"""
<p>给你一棵<strong> 完全二叉树</strong> 的根节点 <code>root</code> ，求出该树的节点个数。</p>

<p><a href="https://baike.baidu.com/item/%E5%AE%8C%E5%85%A8%E4%BA%8C%E5%8F%89%E6%A0%91/7773232?fr=aladdin">完全二叉树</a> 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 <code>h</code> 层，则该层包含 <code>1~&nbsp;2<sup>h</sup></code>&nbsp;个节点。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/14/complete.jpg" style="width: 372px; height: 302px;" /> 
<pre>
<strong>输入：</strong>root = [1,2,3,4,5,6]
<strong>输出：</strong>6
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = []
<strong>输出：</strong>0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [1]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li>树中节点的数目范围是<code>[0, 5 * 10<sup>4</sup>]</code></li> 
 <li><code>0 &lt;= Node.val &lt;= 5 * 10<sup>4</sup></code></li> 
 <li>题目数据保证输入的树是 <strong>完全二叉树</strong></li> 
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>遍历树来统计节点是一种时间复杂度为 <code>O(n)</code> 的简单解决方案。你可以设计一个更快的算法吗？</p>

<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>二分查找</li><li>二叉树</li></div></div><br><div><li>👍 933</li><li>👎 0</li></div>
"""
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def height(self, root: TreeNode):
        height = 0
        while root:
            root = root.left
            height += 1
        return height

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        if leftHeight == rightHeight:
            return (2 ** leftHeight - 1) + self.countNodes(root.right) + 1
        else:
            return (2 ** rightHeight - 1) + self.countNodes(root.left) + 1
# leetcode submit region end(Prohibit modification and deletion)
