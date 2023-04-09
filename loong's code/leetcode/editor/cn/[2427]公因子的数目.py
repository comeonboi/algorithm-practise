"""
<p>给你两个正整数 <code>a</code> 和 <code>b</code> ，返回 <code>a</code> 和 <code>b</code> 的 <strong>公</strong> 因子的数目。</p>

<p>如果 <code>x</code> 可以同时整除 <code>a</code> 和 <code>b</code> ，则认为 <code>x</code> 是 <code>a</code> 和 <code>b</code> 的一个 <strong>公因子</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>a = 12, b = 6
<strong>输出：</strong>4
<strong>解释：</strong>12 和 6 的公因子是 1、2、3、6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>a = 25, b = 30
<strong>输出：</strong>2
<strong>解释：</strong>25 和 30 的公因子是 1、5 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>1 &lt;= a, b &lt;= 1000</code></li> 
</ul>

<div><div>Related Topics</div><div><li>数学</li><li>枚举</li><li>数论</li></div></div><br><div><li>👍 9</li><li>👎 0</li></div>
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                count += 1
        return count
# leetcode submit region end(Prohibit modification and deletion)
