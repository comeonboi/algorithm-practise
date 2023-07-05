def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def recursion(res):
        dummy = ListNode(0)
        ptr = dummy
        for i in res:
            ptr.next = ListNode(i)
            ptr = ptr.next
        return dummy.next

    ls1, ls2 = [], []
    while l1:
        ls1.append(l1.val)
        l1 = l1.next
    while l2:
        ls2.append(l2.val)
        l2 = l2.next

    ss1 = ''.join(str(i) for i in ls1)
    ss2 = ''.join(str(i) for i in ls2)

    res = (int(ss1) + int(ss2))
    new_res = [int(i) for i in str(res)]

    return recursion(new_res)