# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        root=ListNode(0)
        cur=root
        while head:
            if head.val==val:
                head=head.next
                continue
            cur.next=ListNode(head.val)
            head=head.next
            cur=cur.next
        return root.next
