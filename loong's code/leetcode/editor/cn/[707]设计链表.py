"""
<p>你可以选择使用单链表或者双链表，设计并实现自己的链表。</p>

<p>单链表中的节点应该具备两个属性：<code>val</code> 和 <code>next</code> 。<code>val</code> 是当前节点的值，<code>next</code> 是指向下一个节点的指针/引用。</p>

<p>如果是双向链表，则还需要属性&nbsp;<code>prev</code>&nbsp;以指示链表中的上一个节点。假设链表中的所有节点下标从 <strong>0</strong> 开始。</p>

<p>实现 <code>MyLinkedList</code> 类：</p>

<ul> 
 <li><code>MyLinkedList()</code> 初始化 <code>MyLinkedList</code> 对象。</li> 
 <li><code>int get(int index)</code> 获取链表中下标为 <code>index</code> 的节点的值。如果下标无效，则返回 <code>-1</code> 。</li> 
 <li><code>void addAtHead(int val)</code> 将一个值为 <code>val</code> 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。</li> 
 <li><code>void addAtTail(int val)</code> 将一个值为 <code>val</code> 的节点追加到链表中作为链表的最后一个元素。</li> 
 <li><code>void addAtIndex(int index, int val)</code> 将一个值为 <code>val</code> 的节点插入到链表中下标为 <code>index</code> 的节点之前。如果 <code>index</code> 等于链表的长度，那么该节点会被追加到链表的末尾。如果 <code>index</code> 比长度更大，该节点将 <strong>不会插入</strong> 到链表中。</li> 
 <li><code>void deleteAtIndex(int index)</code> 如果下标有效，则删除链表中下标为 <code>index</code> 的节点。</li> 
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例：</strong></p>

<pre>
<strong>输入</strong>
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
<strong>输出</strong>
[null, null, null, null, 2, null, 3]

<strong>解释</strong>
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // 链表变为 1-&gt;2-&gt;3
myLinkedList.get(1);              // 返回 2
myLinkedList.deleteAtIndex(1);    // 现在，链表变为 1-&gt;3
myLinkedList.get(1);              // 返回 3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>0 &lt;= index, val &lt;= 1000</code></li> 
 <li>请不要使用内置的 LinkedList 库。</li> 
 <li>调用 <code>get</code>、<code>addAtHead</code>、<code>addAtTail</code>、<code>addAtIndex</code> 和 <code>deleteAtIndex</code> 的次数不超过 <code>2000</code> 。</li> 
</ul>

<div><div>Related Topics</div><div><li>设计</li><li>链表</li></div></div><br><div><li>👍 798</li><li>👎 0</li></div>
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Node:
    def __init__(self, _val):
        self.val = _val
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.sz = 0

    def get(self, index: int) -> int:
        node = self.getNode(index)
        if node is None:
            return -1
        return node.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.sz += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self.sz += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.sz:
            return
        if index == self.sz:
            self.addAtTail(val)
            return
        if index <= 0:
            self.addAtHead(val)
            return
        else:
            node, cur = Node(val), self.getNode(index)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node
            self.sz += 1

    def deleteAtIndex(self, index: int) -> None:
        node = self.getNode(index)
        if node:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.sz -= 1

    def getNode(self, index):
        isLeft = index <= self.sz // 2
        if not isLeft:
            index = self.sz - index - 1
        cur = self.head.next if isLeft else self.tail.prev
        while cur != self.head and cur != self.tail:
            if index == 0:
                return cur
            index -= 1
            cur = cur.next if isLeft else cur.prev
        return None

# Your MyLinkedList object will be instantiated and called as such
# leetcode submit region end(Prohibit modification and deletion)
