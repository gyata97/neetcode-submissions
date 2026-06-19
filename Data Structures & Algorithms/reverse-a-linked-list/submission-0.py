# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        res = []
        cur = head

        while cur:
           res.append(cur)
           cur = cur.next

        for i in range(len(res)-1, 0, -1):
            res[i].next = res[i-1]

        res[0].next = None
        return res[-1]