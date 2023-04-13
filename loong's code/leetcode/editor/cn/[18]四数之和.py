"""
<p>给你一个由 <code>n</code> 个整数组成的数组&nbsp;<code>nums</code> ，和一个目标值 <code>target</code> 。请你找出并返回满足下述全部条件且<strong>不重复</strong>的四元组&nbsp;<code>[nums[a], nums[b], nums[c], nums[d]]</code>&nbsp;（若两个四元组元素一一对应，则认为两个四元组重复）：</p>

<ul> 
 <li><code>0 &lt;= a, b, c, d&nbsp;&lt; n</code></li> 
 <li><code>a</code>、<code>b</code>、<code>c</code> 和 <code>d</code> <strong>互不相同</strong></li> 
 <li><code>nums[a] + nums[b] + nums[c] + nums[d] == target</code></li> 
</ul>

<p>你可以按 <strong>任意顺序</strong> 返回答案 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,0,-1,0,-2,2], target = 0
<strong>输出：</strong>[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,2,2,2,2], target = 8
<strong>输出：</strong>[[2,2,2,2]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>1 &lt;= nums.length &lt;= 200</code></li> 
 <li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li> 
 <li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li> 
</ul>

<div><div>Related Topics</div><div><li>数组</li><li>双指针</li><li>排序</li></div></div><br><div><li>👍 1567</li><li>👎 0</li></div>
"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# 双指针法
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for k in range(i+1, n):
                if k > i + 1 and nums[k] == nums[k-1]: continue
                p = k + 1
                q = n - 1

                while p < q:
                    if nums[i] + nums[k] + nums[p] + nums[q] > target: q -= 1
                    elif nums[i] + nums[k] + nums[p] + nums[q] < target: p += 1
                    else:
                        res.append([nums[i], nums[k], nums[p], nums[q]])
                        while p < q and nums[p] == nums[p + 1]: p += 1
                        while p < q and nums[q] == nums[q - 1]: q -= 1
                        p += 1
                        q -= 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
