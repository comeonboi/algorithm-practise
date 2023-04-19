"""
<p>给定二叉树的根节点&nbsp;<code>root</code>，找出存在于 <strong>不同</strong> 节点&nbsp;<code>A</code> 和&nbsp;<code>B</code>&nbsp;之间的最大值 <code>V</code>，其中&nbsp;<code>V = |A.val - B.val|</code>，且&nbsp;<code>A</code>&nbsp;是&nbsp;<code>B</code>&nbsp;的祖先。</p>

<p>（如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/11/09/tmp-tree.jpg" style="width: 400px; height: 390px;" /></p>

<pre>
<strong>输入：</strong>root = [8,3,10,1,6,null,14,null,null,4,7,13]
<strong>输出：</strong>7
<strong>解释： </strong>
我们有大量的节点与其祖先的差值，其中一些如下：
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
在所有可能的差值中，最大值 7 由 |8 - 1| = 7 得出。
</pre>

<p><strong>示例 2：</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/09/tmp-tree-1.jpg" style="width: 250px; height: 349px;" /> 
<pre>
<strong>输入：</strong>root = [1,null,2,null,0,3]
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li>树中的节点数在&nbsp;<code>2</code>&nbsp;到&nbsp;<code>5000</code>&nbsp;之间。</li> 
 <li><code>0 &lt;= Node.val &lt;= 10<sup>5</sup></code></li> 
</ul>

<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>二叉树</li></div></div><br><div><li>👍 171</li><li>👎 0</li></div>
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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode]) -> (int, int):
            if node is None:
                return inf, -inf  # 保证空节点不影响 mn 和 mx
            mn = mx = node.val
            l_mn, l_mx = dfs(node.left)
            r_mn, r_mx = dfs(node.right)
            mn = min(mn, l_mn, r_mn)
            mx = max(mx, l_mx, r_mx)
            nonlocal ans
            ans = max(ans, node.val - mn, mx - node.val)
            return mn, mx
        dfs(root)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
