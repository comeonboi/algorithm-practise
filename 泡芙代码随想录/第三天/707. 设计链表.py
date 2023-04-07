class ListNode:
    def __init__(self, val=0, next=None, pre=None):
        self.val = val
        self.next = next
        self.pre = pre


class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index + 1 > self.size:
            return -1
        n = 0
        now = self.head
        while (n < index):
            now = now.next
            n += 1
        return now.val

    def addAtHead(self, val: int) -> None:
        temp = self.head
        self.head = ListNode(val, temp)
        temp.pre = self.head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.head = ListNode(val)
            self.size += 1
            return None
        n = 1
        now = self.head
        while (n < self.size):
            now = now.next
            n += 1
        now.next = ListNode(val, None, now)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
            return None
        if index == 0:
            self.addAtHead(val)
            return None
        if index + 1 > self.size:
            return None
        n = 0
        now = self.head
        while (n < index):
            now = now.next
            n += 1
        tPre = now.pre
        now.pre = ListNode(val, now, tPre)
        tPre.next = now.pre
        self.size += 1
        n = 0
        now = self.head

    def deleteAtIndex(self, index: int) -> None:
        if index + 1 > self.size:
            return None
        n = 0
        now = self.head
        while (n < index):
            now = now.next
            n += 1
        if n == 0:
            self.head = now.next
            if self.head != None:
                self.head.pre = None
            self.size -= 1
            return None
        preNode = now.pre
        nextNode = now.next
        if preNode != None:
            preNode.next = nextNode
        if nextNode != None:
            nextNode.pre = preNode
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)