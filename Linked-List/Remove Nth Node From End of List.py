# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        a=[]
        while cur:
            a.append(cur.val)
            cur=cur.next
        a.pop(len(a)-n)
        if not a:
            return None
        dummy=ListNode(a[0])
        temp=dummy
        for i in a[1:]:
            temp.next=ListNode(i)
            temp=temp.next
        return dummy