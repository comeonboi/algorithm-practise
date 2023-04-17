"""
<p>给你一个整数数组 <code>nums</code>，有一个大小为&nbsp;<code>k</code><em>&nbsp;</em>的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 <code>k</code>&nbsp;个数字。滑动窗口每次只向右移动一位。</p>

<p>返回 <em>滑动窗口中的最大值 </em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,3,-1,-3,5,3,6,7], k = 3
<b>输出：</b>[3,3,5,5,6,7]
<b>解释：</b>
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       <strong>3</strong>
 1 [3  -1  -3] 5  3  6  7       <strong>3</strong>
 1  3 [-1  -3  5] 3  6  7      <strong> 5</strong>
 1  3  -1 [-3  5  3] 6  7       <strong>5</strong>
 1  3  -1  -3 [5  3  6] 7       <strong>6</strong>
 1  3  -1  -3  5 [3  6  7]      <strong>7</strong>
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1], k = 1
<b>输出：</b>[1]
</pre>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul> 
 <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li> 
 <li><code>-10<sup>4</sup>&nbsp;&lt;= nums[i] &lt;= 10<sup>4</sup></code></li> 
 <li><code>1 &lt;= k &lt;= nums.length</code></li> 
</ul>

<div><div>Related Topics</div><div><li>队列</li><li>数组</li><li>滑动窗口</li><li>单调队列</li><li>堆（优先队列）</li></div></div><br><div><li>👍 2248</li><li>👎 0</li></div>
"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        queue = []  # 维护一个单调递减队列，队首元素为当前窗口的最大值
        for i in range(n):
            if i >= k and queue[0] == nums[i-k]:
                queue.pop(0)  # 窗口向右移动一位，弹出队首元素
            while queue and queue[-1] < nums[i]:
                queue.pop()  # 弹出队列中比新元素小的元素
            queue.append(nums[i])  # 添加新元素到队列中
            if i >= k - 1:
                ans.append(queue[0])  # 将队列的第一个元素作为当前窗口的最大值
        return ans

# leetcode submit region end(Prohibit modification and deletion)
print(Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))