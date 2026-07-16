from collections import Counter
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        if not a:
            return None
        b=Counter(a)
        root=ListNode()
        t=root
        for i in b:
            if b[i]==1:
                t.next=ListNode(i)
                t=t.next
        return root.next