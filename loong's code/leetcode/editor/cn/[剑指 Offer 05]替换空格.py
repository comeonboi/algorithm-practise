"""
<p>请实现一个函数，把字符串 <code>s</code> 中的每个空格替换成"%20"。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = "We are happy."
<strong>输出：</strong>"We%20are%20happy."</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<p><code>0 &lt;= s 的长度 &lt;= 10000</code></p>

<div><div>Related Topics</div><div><li>字符串</li></div></div><br><div><li>👍 455</li><li>👎 0</li></div>
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")
# leetcode submit region end(Prohibit modification and deletion)
