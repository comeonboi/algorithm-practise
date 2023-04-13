"""
<p>给你一个整数数组 <code>nums</code> ，返回出现最频繁的偶数元素。</p>

<p>如果存在多个满足条件的元素，只需要返回 <strong>最小</strong> 的一个。如果不存在这样的元素，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [0,1,2,2,4,4,1]
<strong>输出：</strong>2
<strong>解释：</strong>
数组中的偶数元素为 0、2 和 4 ，在这些元素中，2 和 4 出现次数最多。
返回最小的那个，即返回 2 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [4,4,4,9,2,4]
<strong>输出：</strong>4
<strong>解释：</strong>4 是出现最频繁的偶数元素。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [29,47,21,41,13,37,25,7]
<strong>输出：</strong>-1
<strong>解释：</strong>不存在偶数元素。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>1 &lt;= nums.length &lt;= 2000</code></li> 
 <li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li> 
</ul>

<div><div>Related Topics</div><div><li>数组</li><li>哈希表</li><li>计数</li></div></div><br><div><li>👍 43</li><li>👎 0</li></div>
"""
from collections import Counter
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_num = list(filter(lambda x: x%2 == 0, nums))
        counts = Counter(even_num)
        if not even_num:
            return -1
        max_count = max(counts.values())
        most_frequent = [num for num, count in counts.items() if count == max_count]
        return min(most_frequent)
