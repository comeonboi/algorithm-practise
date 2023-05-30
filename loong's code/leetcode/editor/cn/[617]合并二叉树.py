"""
<p>给你两棵二叉树： <code>root1</code> 和 <code>root2</code> 。</p>

<p>想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，<strong>不为</strong> null 的节点将直接作为新二叉树的节点。</p>

<p>返回合并后的二叉树。</p>

<p><strong>注意:</strong> 合并过程必须从两个树的根节点开始。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/merge.jpg" style="height: 163px; width: 600px;" /> 
<pre>
<strong>输入：</strong>root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
<strong>输出：</strong>[3,4,5,5,4,null,7]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root1 = [1], root2 = [1,2]
<strong>输出：</strong>[2,2]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li>两棵树中的节点数目在范围 <code>[0, 2000]</code> 内</li> 
 <li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li> 
</ul>

<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>广度优先搜索</li><li>二叉树</li></div></div><br><div><li>👍 1235</li><li>👎 0</li></div>
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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        new_tree = TreeNode()
        if not root1 and not root2:
            return None
        if not root1: return root2
        if not root2: return root1

        # x看便利第一个茶树
        def recursion(node1, node2):
            if not (node1 and node2):
                return node1 if node1 else node2
            node1.val = node1.val + node2.val
            node1.left = recursion(node1.left, node2.left)
            node1.right = recursion(node1.right, node2.right)
            return node1
        return recursion(root1, root2)
# leetcode submit region end(Prohibit modification and deletion)
