/**
<p>给你两个&nbsp;<strong>非空</strong> 的链表，表示两个非负的整数。它们每位数字都是按照&nbsp;<strong>逆序</strong>&nbsp;的方式存储的，并且每个节点只能存储&nbsp;<strong>一位</strong>&nbsp;数字。</p>

<p>请你将两个数相加，并以相同形式返回一个表示和的链表。</p>

<p>你可以假设除了数字 0 之外，这两个数都不会以 0&nbsp;开头。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg" style="width: 483px; height: 342px;" />
<pre>
<strong>输入：</strong>l1 = [2,4,3], l2 = [5,6,4]
<strong>输出：</strong>[7,0,8]
<strong>解释：</strong>342 + 465 = 807.
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>l1 = [0], l2 = [0]
<strong>输出：</strong>[0]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>输出：</strong>[8,9,9,9,0,0,0,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
 <li>每个链表中的节点数在范围 <code>[1, 100]</code> 内</li>
 <li><code>0 &lt;= Node.val &lt;= 9</code></li>
 <li>题目数据保证列表表示的数字不含前导零</li>
</ul>

<div><div>Related Topics</div><div><li>递归</li><li>链表</li><li>数学</li></div></div><br><div><li>👍 9712</li><li>👎 0</li></div>
*/

//leetcode submit region begin(Prohibit modification and deletion)

//package main
//
//type ListNode struct {
//	Val  int
//	Next *ListNode
//}

func addTwo(l1 *ListNode, l2 *ListNode, carry int) *ListNode {
	if l1 == nil && l2 == nil {
		if carry != 0 {
			return &ListNode{Val: carry}
		}
		return nil
	}
	if l1 == nil {
		l1, l2 = l2, l1
	}
	carry += l1.Val
	if l2 != nil {
		carry += l2.Val
		l2 = l2.Next
	}
	l1.Val = carry % 10
	l1.Next = addTwo(l1.Next, l2, carry/10)
	return l1
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	return addTwo(l1, l2, 0)
}

//leetcode submit region end(Prohibit modification and deletion)
