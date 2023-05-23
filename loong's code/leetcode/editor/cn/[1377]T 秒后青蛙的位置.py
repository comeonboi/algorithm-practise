"""
<p>给你一棵由 <code>n</code> 个顶点组成的无向树，顶点编号从 <code>1</code> 到 <code>n</code>。青蛙从 <strong>顶点 1</strong> 开始起跳。规则如下：</p>

<ul> 
 <li>在一秒内，青蛙从它所在的当前顶点跳到另一个 <strong>未访问</strong> 过的顶点（如果它们直接相连）。</li> 
 <li>青蛙无法跳回已经访问过的顶点。</li> 
 <li>如果青蛙可以跳到多个不同顶点，那么它跳到其中任意一个顶点上的机率都相同。</li> 
 <li>如果青蛙不能跳到任何未访问过的顶点上，那么它每次跳跃都会停留在原地。</li> 
</ul>

<p>无向树的边用数组 <code>edges</code> 描述，其中 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 意味着存在一条直接连通 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 两个顶点的边。</p>

<p>返回青蛙在 <em><code>t</code></em> 秒后位于目标顶点 <em><code>target</code> </em>上的概率。与实际答案相差不超过 <code>10<sup>-5</sup></code> 的结果将被视为正确答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/12/21/frog1.jpg" /></p>

<pre>
<strong>输入：</strong>n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
<strong>输出：</strong>0.16666666666666666 
<strong>解释：</strong>上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，第 <strong>1 秒</strong> 有 1/3 的概率跳到顶点 2 ，然后第 <strong>2 秒</strong> 有 1/2 的概率跳到顶点 4，因此青蛙在 2 秒后位于顶点 4 的概率是 1/3 * 1/2 = 1/6 = 0.16666666666666666 。 
</pre>

<p><strong>示例 2：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/12/21/frog2.jpg" /></p>

<pre>
<strong>输入：</strong>n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
<strong>输出：</strong>0.3333333333333333
<strong>解释：</strong>上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，有 1/3 = 0.3333333333333333 的概率能够 <strong>1 秒</strong> 后跳到顶点 7 。 
</pre>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>1 &lt;= n &lt;= 100</code></li> 
 <li><code>edges.length == n - 1</code></li> 
 <li><code>edges[i].length == 2</code></li> 
 <li><code>1 &lt;= a<sub>i</sub>, b<sub>i</sub>&nbsp;&lt;= n</code></li> 
 <li><code>1 &lt;= t &lt;= 50</code></li> 
 <li><code>1 &lt;= target &lt;= n</code></li> 
</ul>

<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>广度优先搜索</li><li>图</li></div></div><br><div><li>👍 54</li><li>👎 0</li></div>
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
# leetcode submit region end(Prohibit modification and deletion)
