"""
<p>编写一个算法来判断一个数 <code>n</code> 是不是快乐数。</p>

<p><strong>「快乐数」</strong>&nbsp;定义为：</p>

<ul> 
 <li>对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。</li> 
 <li>然后重复这个过程直到这个数变为 1，也可能是 <strong>无限循环</strong> 但始终变不到 1。</li> 
 <li>如果这个过程 <strong>结果为</strong>&nbsp;1，那么这个数就是快乐数。</li> 
</ul>

<p>如果 <code>n</code> 是 <em>快乐数</em> 就返回 <code>true</code> ；不是，则返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 19
<strong>输出：</strong>true
<strong>解释：
</strong>1<sup>2</sup> + 9<sup>2</sup> = 82
8<sup>2</sup> + 2<sup>2</sup> = 68
6<sup>2</sup> + 8<sup>2</sup> = 100
1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li> 
</ul>

<div><div>Related Topics</div><div><li>哈希表</li><li>数学</li><li>双指针</li></div></div><br><div><li>👍 1278</li><li>👎 0</li></div>
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isHappy(self, n: int) -> bool:
        list1 = []
        ans = n
        while 1:
            ans = list(map(int, list(str(ans))))
            ans = sum(map(lambda x: x ** 2, ans))
            if ans == 1:
                return True
            if ans not in list1:
                list1.append(ans)
            else:
                return False

# leetcode submit region end(Prohibit modification and deletion)
