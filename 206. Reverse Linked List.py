class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 5 4 3 2 1
class Solution:
    def reverseList(self, head):
        return self.recursive(head, None)
    def recursive(self, node, prev):
        if not node: return prev
        cur = ListNode(node.val)
        cur.next = prev
        return self.recursive(node.next, cur)
rt = ListNode(5)
rt.next = ListNode(4)
rt.next.next = ListNode(3)
rt.next.next.next = ListNode(2)
rt.next.next.next.next = ListNode(1)
rt.next.next.next.next.next = None
s = Solution()
print(s.reverseList(rt))