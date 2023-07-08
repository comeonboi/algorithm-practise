"""
<p>袋子中装有一些物品，每个物品上都标记着数字 <code>1</code> 、<code>0</code> 或 <code>-1</code> 。</p>

<p>给你四个非负整数 <code>numOnes</code> 、<code>numZeros</code> 、<code>numNegOnes</code> 和 <code>k</code> 。</p>

<p>袋子最初包含：</p>

<ul> 
 <li><code>numOnes</code> 件标记为 <code>1</code> 的物品。</li> 
 <li><code>numZeroes</code> 件标记为 <code>0</code> 的物品。</li> 
 <li><code>numNegOnes</code> 件标记为 <code>-1</code> 的物品。</li> 
</ul>

<p>现计划从这些物品中恰好选出 <code>k</code> 件物品。返回所有可行方案中，物品上所标记数字之和的最大值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2
<strong>输出：</strong>2
<strong>解释：</strong>袋子中的物品分别标记为 {1, 1, 1, 0, 0} 。取 2 件标记为 1 的物品，得到的数字之和为 2 。
可以证明 2 是所有可行方案中的最大值。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4
<strong>输出：</strong>3
<strong>解释：</strong>袋子中的物品分别标记为 {1, 1, 1, 0, 0} 。取 3 件标记为 1 的物品，1 件标记为 0 的物品，得到的数字之和为 3 。
可以证明 3 是所有可行方案中的最大值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>0 &lt;= numOnes, numZeros, numNegOnes &lt;= 50</code></li> 
 <li><code>0 &lt;= k &lt;= numOnes + numZeros + numNegOnes</code></li> 
</ul>

<div><div>Related Topics</div><div><li>贪心</li><li>数学</li></div></div><br><div><li>👍 37</li><li>👎 0</li></div>
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        if k <= numOnes:
            ans+=k
            return ans
        else:
            k -= numOnes
            ans += numOnes
            if k <= numZeros:
                return ans
            else:
                k -= numZeros
                ans -= k
                return ans
