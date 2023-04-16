"""
<p>给定一个只包括 <code>'('</code>，<code>')'</code>，<code>'{'</code>，<code>'}'</code>，<code>'['</code>，<code>']'</code>&nbsp;的字符串 <code>s</code> ，判断字符串是否有效。</p>

<p>有效字符串需满足：</p>

<ol> 
 <li>左括号必须用相同类型的右括号闭合。</li> 
 <li>左括号必须以正确的顺序闭合。</li> 
 <li>每个右括号都有一个对应的相同类型的左括号。</li> 
</ol>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "()"
<strong>输出：</strong>true
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>s = "()[]{}"
<strong>输出：</strong>true
</pre>

<p><strong>示例&nbsp;3：</strong></p>

<pre>
<strong>输入：</strong>s = "(]"
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li> 
 <li><code>s</code> 仅由括号 <code>'()[]{}'</code> 组成</li> 
</ul>

<div><div>Related Topics</div><div><li>栈</li><li>字符串</li></div></div><br><div><li>👍 3876</li><li>👎 0</li></div>
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = ["?"]

        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        for i in s:
            if i in dic:
                stack.append(i)
            elif dic[stack.pop()] != i:
                return False
        return len(stack) == 1
# leetcode submit region end(Prohibit modification and deletion)
