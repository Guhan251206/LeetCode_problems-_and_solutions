# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        root=ListNode(head.val)
        cur=root
        head=head.next

        while head:
            if cur.val==head.val:
                head=head.next
                continue
            cur.next=ListNode(head.val)
            head=head.next
            cur=cur.next
            
        return root