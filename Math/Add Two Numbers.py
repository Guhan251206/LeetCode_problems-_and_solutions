# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1=l1
        s1=''
        while r1:
            s1+=str(r1.val)
            r1=r1.next
        r2=l2
        s2=''
        while r2:
            s2+=str(r2.val)
            r2=r2.next
        t=str(int(s1[::-1])+int(s2[::-1]))[::-1]
        root=ListNode()
        temp=root
        for ch in t:
            temp.next=ListNode(int(ch))
            temp=temp.next
        
        return root.next
