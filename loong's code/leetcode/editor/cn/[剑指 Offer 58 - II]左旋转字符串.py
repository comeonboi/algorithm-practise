"""
<p>字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入:</strong> s = "abcdefg", k = 2
<strong>输出:&nbsp;</strong>"cdefgab"
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入:</strong> s = "lrloseumgh", k = 6
<strong>输出:&nbsp;</strong>"umghlrlose"
</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<ul> 
 <li><code>1 &lt;= k &lt; s.length &lt;= 10000</code></li> 
</ul>

<div><div>Related Topics</div><div><li>数学</li><li>双指针</li><li>字符串</li></div></div><br><div><li>👍 383</li><li>👎 0</li></div>
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = list(s)
        return ''.join(s[n:] + s[:n])
# leetcode submit region end(Prohibit modification and deletion)
