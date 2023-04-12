/**
<p>Given two integer arrays <code>nums1</code> and <code>nums2</code>, return <em>an array of their intersection</em>. Each element in the result must be <strong>unique</strong> and you may return the result in <strong>any order</strong>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,2,1], nums2 = [2,2]
<strong>Output:</strong> [2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>Output:</strong> [9,4]
<strong>Explanation:</strong> [4,9] is also accepted.
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li> 
 <li><code>0 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li> 
</ul>

<div><div>Related Topics</div><div><li>数组</li><li>哈希表</li><li>双指针</li><li>二分查找</li><li>排序</li></div></div><br><div><li>👍 747</li><li>👎 0</li></div>
*/
#include "main.h"
//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        // 哈希表
        unordered_set<int> record(nums1.begin(), nums1.end());
        vector<int> res;
        for(auto iter: nums2){
            if (record.find(iter) != record.end()){
                res.push_back(iter);
                record.erase(iter);
            }
        }
        return res;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
