"""
<p>给你一个长度为 <code>n</code> 的整数数组&nbsp;<code>nums</code><em>&nbsp;</em>和 一个目标值&nbsp;<code>target</code>。请你从 <code>nums</code><em> </em>中选出三个整数，使它们的和与&nbsp;<code>target</code>&nbsp;最接近。</p>

<p>返回这三个数的和。</p>

<p>假定每组输入只存在恰好一个解。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1,2,1,-4], target = 1
<strong>输出：</strong>2
<strong>解释：</strong>与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,0,0], target = 1
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>3 &lt;= nums.length &lt;= 1000</code></li> 
 <li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li> 
 <li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li> 
</ul>

<div><div>Related Topics</div><div><li>数组</li><li>双指针</li><li>排序</li></div></div><br><div><li>👍 1449</li><li>👎 0</li></div>
"""
from cmath import inf
from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # -1,1,2,-4
        best = inf
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur
        for ind in range(len(nums)):
            # 和上一次元素不等
            if ind > 0 and nums[ind] == nums[ind - 1]:
                continue
            j, k = ind + 1, len(nums) - 1
            while j < k:
                s = nums[ind] + nums[j] + nums[k]
                if s == target:
                    return target
                update(s)
                if s > target:
                    # 移动k到下一个不相等的元素
                    k0 = k - 1
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                else:
                    j0 = j + 1
                    while j0 <k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0
        return best
# leetcode submit region end(Prohibit modification and deletion)
