"""
<p>给定一个长度为&nbsp;<code>n</code>&nbsp;的链表&nbsp;<code>head</code></p>

<p>对于列表中的每个节点，查找下一个 <strong>更大节点</strong> 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值 <strong>严格大于</strong> 它的值。</p>

<p>返回一个整数数组 <code>answer</code> ，其中 <code>answer[i]</code> 是第 <code>i</code> 个节点( <strong>从1开始</strong> )的下一个更大的节点的值。如果第 <code>i</code> 个节点没有下一个更大的节点，设置&nbsp;<code>answer[i] = 0</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/08/05/linkedlistnext1.jpg" /></p>

<pre>
<strong>输入：</strong>head = [2,1,5]
<strong>输出：</strong>[5,5,0]
</pre>

<p><strong>示例 2：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/08/05/linkedlistnext2.jpg" /></p>

<pre>
<strong>输入：</strong>head = [2,7,4,3,5]
<strong>输出：</strong>[7,0,5,5,0]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li>链表中节点数为&nbsp;<code>n</code></li> 
 <li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li> 
 <li><code>1 &lt;= Node.val &lt;= 10<sup>9</sup></code></li> 
</ul>

<div><div>Related Topics</div><div><li>栈</li><li>数组</li><li>链表</li><li>单调栈</li></div></div><br><div><li>👍 294</li><li>👎 0</li></div>
"""
from typing import Optional, List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        st = []  # 单调栈（节点值，节点下标）
        while head:
            while st and st[-1][0] < head.val:
                ans[st.pop()[1]] = head.val  # 用当前节点值更新答案
            st.append((head.val, len(ans)))  # 当前 ans 的长度就是当前节点的下标
            ans.append(0)  # 占位
            head = head.next
        return ans

# class Solution:
#     def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
#         if not head:
#             return []
#         if not head.next:
#             return [0]
#         stack = []
#         ans = []
#         ind = 0
#         while head:
#             i = 0
#             stack.append([head.val, ind])
#             while True:
#                 if head.val > stack[i][0]:
#                     ans.append([head.val, stack[i][1]])
#                     stack.pop(i)
#                 else:
#                     i += 1
#                 if i >= len(stack):
#                     break
#             head = head.next
#             ind += 1
#         print(ind)
#         ans2 = [0] * ind
#         for [i, j] in stack:
#             ans2[j] = 0
#         for [i, j] in ans:
#             ans2[j] = i
#         # while stack:
#         #     ans.insert(stack[0][1]-1, 0)
#         #     stack.pop()
#         return ans2
# leetcode submit region end(Prohibit modification and deletion)
