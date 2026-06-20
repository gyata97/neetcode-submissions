# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ll = []
        cur = head

        while cur:
            ll.append(cur)
            cur = cur.next

        idx = len(ll) - n
        if idx == 0:
            return head.next
        ll[idx - 1].next = ll[idx].next

        return head