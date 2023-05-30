"""
<p>给你一个字符串数组 <code>words</code>&nbsp;，每一个字符串长度都相同，令所有字符串的长度都为 <code>n</code>&nbsp;。</p>

<p>每个字符串&nbsp;<code>words[i]</code>&nbsp;可以被转化为一个长度为&nbsp;<code>n - 1</code>&nbsp;的&nbsp;<strong>差值整数数组</strong>&nbsp;<code>difference[i]</code>&nbsp;，其中对于&nbsp;<code>0 &lt;= j &lt;= n - 2</code>&nbsp;有&nbsp;<code>difference[i][j] = words[i][j+1] - words[i][j]</code>&nbsp;。注意两个字母的差值定义为它们在字母表中&nbsp;<strong>位置</strong>&nbsp;之差，也就是说&nbsp;<code>'a'</code>&nbsp;的位置是&nbsp;<code>0</code>&nbsp;，<code>'b'</code>&nbsp;的位置是&nbsp;<code>1</code>&nbsp;，<code>'z'</code>&nbsp;的位置是&nbsp;<code>25</code>&nbsp;。</p>

<ul> 
 <li>比方说，字符串&nbsp;<code>"acb"</code>&nbsp;的差值整数数组是&nbsp;<code>[2 - 0, 1 - 2] = [2, -1]</code>&nbsp;。</li> 
</ul>

<p><code>words</code>&nbsp;中所有字符串 <strong>除了一个字符串以外</strong>&nbsp;，其他字符串的差值整数数组都相同。你需要找到那个不同的字符串。</p>

<p>请你返回<em>&nbsp;</em><code>words</code>中&nbsp;<strong>差值整数数组</strong>&nbsp;不同的字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>words = ["adc","wzy","abc"]
<b>输出：</b>"abc"
<b>解释：</b>
- "adc" 的差值整数数组是 [3 - 0, 2 - 3] = [3, -1] 。
- "wzy" 的差值整数数组是 [25 - 22, 24 - 25]= [3, -1] 。
- "abc" 的差值整数数组是 [1 - 0, 2 - 1] = [1, 1] 。
不同的数组是 [1, 1]，所以返回对应的字符串，"abc"。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>words = ["aaa","bob","ccc","ddd"]
<b>输出：</b>"bob"
<b>解释：</b>除了 "bob" 的差值整数数组是 [13, -13] 以外，其他字符串的差值整数数组都是 [0, 0] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>3 &lt;= words.length &lt;= 100</code></li> 
 <li><code>n == words[i].length</code></li> 
 <li><code>2 &lt;= n &lt;= 20</code></li> 
 <li><code>words[i]</code>&nbsp;只含有小写英文字母。</li> 
</ul>

<div><div>Related Topics</div><div><li>数组</li><li>哈希表</li><li>字符串</li></div></div><br><div><li>👍 48</li><li>👎 0</li></div>
"""
from collections import defaultdict
from itertools import pairwise
from typing import List
import icecream

# leetcode submit region begin(Prohibit modification and deletion)
# codelass Solution:
#     def oddString(self, words: List[str]) -> str:
#         how_many_words = len(words)
#         words2 = list(zip(*words))
#         ans = set()
#         for i in range(1, how_many_words):
#             for j in range(len(words2[0])):
#                 value = ord(words2[i][j]) - ord(words2[i - 1][j])
#                 icecream.ic(ord(words2[i][j]) - ord(words2[i - 1][j]))
#                 if value not in ans and len(ans) != 0:
#                     return value
#                 elif value in ans and len(ans) > 1:
#                     ans.remove(value)
#                     # return str(ans)
#                 icecream.ic(ans)
#                 icecream.ic(words2[i][j], words2[i - 1][j])
class Solution:
    def oddString(self, words: List[str]) -> str:
        d = defaultdict(list)
        for s in words:
            t = tuple(ord(b) - ord(a) for a, b in pairwise(s))
            d[t].append(s)
        return next(ss[0] for ss in d.values() if len(ss) == 1)


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().oddString(["adc", "wzy", "abc"]))
