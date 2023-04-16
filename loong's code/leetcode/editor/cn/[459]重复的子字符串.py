"""
<p>给定一个非空的字符串
 <meta charset="UTF-8" />&nbsp;<code>s</code>&nbsp;，检查是否可以通过由它的一个子串重复多次构成。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> s = "abab"
<strong>输出:</strong> true
<strong>解释:</strong> 可由子串 "ab" 重复两次构成。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> s = "aba"
<strong>输出:</strong> false
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> s = "abcabcabcabc"
<strong>输出:</strong> true
<strong>解释:</strong> 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)
</pre>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<p>
 <meta charset="UTF-8" /></p>

<ul> 
 <li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li> 
 <li><code>s</code>&nbsp;由小写英文字母组成</li> 
</ul>

<div><div>Related Topics</div><div><li>字符串</li><li>字符串匹配</li></div></div><br><div><li>👍 944</li><li>👎 0</li></div>
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]  # 返回s是否在s+s中，且s+s中的s不是s+s的首尾元素，因为
# leetcode submit region end(Prohibit modification and deletion)
