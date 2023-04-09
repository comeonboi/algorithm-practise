"""
<p>给你一个正整数&nbsp;<code>n</code> ，生成一个包含 <code>1</code> 到&nbsp;<code>n<sup>2</sup></code>&nbsp;所有元素，且元素按顺时针顺序螺旋排列的&nbsp;<code>n x n</code> 正方形矩阵 <code>matrix</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg" style="width: 242px; height: 242px;" /> 
<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>[[1,2,3],[8,9,4],[7,6,5]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>[[1]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>1 &lt;= n &lt;= 20</code></li> 
</ul>

<div><div>Related Topics</div><div><li>数组</li><li>矩阵</li><li>模拟</li></div></div><br><div><li>👍 1013</li><li>👎 0</li></div>
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        num, target = 1, n * n
        while num <= target:
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        return matrix

# leetcode submit region end(Prohibit modification and deletion)
