from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        if not a:
            return None
        n=len(a)
        def rev(l,r):
            while l<r:
                a[l],a[r]=a[r],a[l]
                l+=1
                r-=1
        k=k%n
        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1)
        root=ListNode(a[0])
        cur=root
        for i in range(1,len(a)):
            cur.next=ListNode(a[i])
            cur=cur.next
        return root