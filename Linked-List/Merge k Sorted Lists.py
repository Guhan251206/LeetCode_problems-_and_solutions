# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a=[]
        for list in lists:
            while list:
                a.append(list.val)
                list=list.next
        if not a:
            return None
        a.sort()
        root=ListNode(a[0])
        temp=root
        for i in a[1:]:
            temp.next=ListNode(i)
            temp=temp.next
        return root