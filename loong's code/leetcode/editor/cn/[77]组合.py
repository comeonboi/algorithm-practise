"""
<p>给定两个整数 <code>n</code> 和 <code>k</code>，返回范围 <code>[1, n]</code> 中所有可能的 <code>k</code> 个数的组合。</p>

<p>你可以按 <strong>任何顺序</strong> 返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 4, k = 2
<strong>输出：</strong>
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1, k = 1
<strong>输出：</strong>[[1]]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>1 &lt;= n &lt;= 20</code></li> 
 <li><code>1 &lt;= k &lt;= n</code></li> 
</ul>

<div><div>Related Topics</div><div><li>回溯</li></div></div><br><div><li>👍 1409</li><li>👎 0</li></div>
"""
from typing import List
import itertools
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.dfs(range(1, n+1), k, [], ans)
        return ans

    def dfs(self, nums, k, path, ans):
        if k == 0:
            ans.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k-1, path+[nums[i]], ans)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        for i in itertools.combinations(range(1,n+1), k):
            ans.append(list(i))
        return ans
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().combine(4,2))