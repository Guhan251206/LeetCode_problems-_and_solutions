# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        i=0
        while i<len(a):
            j=i+k-1
            if j>=len(a):
                break
            l=i
            r=j
            while l<r:
                a[l],a[r]=a[r],a[l]
                l+=1
                r-=1
            i=j+1
        root=ListNode(a[0])
        t=root
        for i in a[1:]:
            t.next=ListNode(i)
            t=t.next
        return root