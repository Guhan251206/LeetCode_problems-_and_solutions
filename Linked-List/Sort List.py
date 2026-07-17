# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        if not a:
            return None
        a.sort()
        root=ListNode(a[0])
        t=root
        for i in a[1:]:
            t.next=ListNode(i)
            t=t.next
        return root