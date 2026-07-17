# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        if not a:
            return None
        l=left-1
        r=right-1
        while l<r:
            a[l],a[r]=a[r],a[l]
            l+=1
            r-=1
        root=ListNode(a[0])
        t=root
        for i in a[1:]:
            t.next=ListNode(i)
            t=t.next
        return root