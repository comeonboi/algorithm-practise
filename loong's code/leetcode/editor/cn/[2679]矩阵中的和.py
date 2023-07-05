"""
<p>给你一个下标从 <strong>0</strong>&nbsp;开始的二维整数数组&nbsp;<code>nums</code>&nbsp;。一开始你的分数为&nbsp;<code>0</code>&nbsp;。你需要执行以下操作直到矩阵变为空：</p>

<ol> 
 <li>矩阵中每一行选取最大的一个数，并删除它。如果一行中有多个最大的数，选择任意一个并删除。</li> 
 <li>在步骤 1 删除的所有数字中找到最大的一个数字，将它添加到你的 <strong>分数</strong>&nbsp;中。</li> 
</ol>

<p>请你返回最后的 <strong>分数</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
<b>输出：</b>15
<b>解释：</b>第一步操作中，我们删除 7 ，6 ，6 和 3 ，将分数增加 7 。下一步操作中，删除 2 ，4 ，5 和 2 ，将分数增加 5 。最后删除 1 ，2 ，3 和 1 ，将分数增加 3 。所以总得分为 7 + 5 + 3 = 15 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [[1]]
<b>输出：</b>1
<b>解释：</b>我们删除 1 并将分数增加 1 ，所以返回 1 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>1 &lt;= nums.length &lt;= 300</code></li> 
 <li><code>1 &lt;= nums[i].length &lt;= 500</code></li> 
 <li><code>0 &lt;= nums[i][j] &lt;= 10<sup>3</sup></code></li> 
</ul>

<div><div>Related Topics</div><div><li>数组</li><li>矩阵</li><li>排序</li><li>模拟</li><li>堆（优先队列）</li></div></div><br><div><li>👍 38</li><li>👎 0</li></div>
"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for ind, i in enumerate(nums):
            nums[ind].sort()
        return sum(max(i) for i in zip(*nums))

        # while len(nums) != 0:
        #     for ind, i in enumerate(nums):
        #         num += i.pop(i.index(max(i)))
        #         if not i:
        #             nums.pop(ind)
        #             break
        # return num

# leetcode submit region end(Prohibit modification and deletion)
print(Solution().matrixSum([[7,2,1],[6,4,2],[6,5,3],[3,2,1]]))