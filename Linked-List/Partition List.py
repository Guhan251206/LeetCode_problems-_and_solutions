# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        if not a:
            return None
        b=[]
        b1=[]
        for i in range(len(a)):
            if a[i]<x:
                b.append(a[i])
            else:
                b1.append(a[i])
        arr=b+b1
        root=ListNode(arr[0])
        t=root
        for x in arr[1:]:
            t.next=ListNode(x)
            t=t.next
        return root