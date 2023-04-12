/**
<p>Write an algorithm to determine if a number <code>n</code> is happy.</p>

<p>A <strong>happy number</strong> is a number defined by the following process:</p>

<ul> 
 <li>Starting with any positive integer, replace the number by the sum of the squares of its digits.</li> 
 <li>Repeat the process until the number equals 1 (where it will stay), or it <strong>loops endlessly in a cycle</strong> which does not include 1.</li> 
 <li>Those numbers for which this process <strong>ends in 1</strong> are happy.</li> 
</ul>

<p>Return <code>true</code> <em>if</em> <code>n</code> <em>is a happy number, and</em> <code>false</code> <em>if not</em>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 19
<strong>Output:</strong> true
<strong>Explanation:</strong>
1<sup>2</sup> + 9<sup>2</sup> = 82
8<sup>2</sup> + 2<sup>2</sup> = 68
6<sup>2</sup> + 8<sup>2</sup> = 100
1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li> 
</ul>

<div><div>Related Topics</div><div><li>哈希表</li><li>数学</li><li>双指针</li></div></div><br><div><li>👍 1278</li><li>👎 0</li></div>
*/
#include "main.h"
//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int getSum(int n){
        int sum = 0;
        while (n!=0){
            sum += (n%10) * (n % 10);
            n = n/10;
        }
        return sum;
    }
    bool isHappy(int n) {
        unordered_set<int> set;
        while(1){
            int sum = getSum(n);
            if (sum==1) return true;
            if (set.find(sum) != set.end()) return false;
            else set.insert(sum);
            n = sum;
        }
    }
};
//leetcode submit region end(Prohibit modification and deletion)
