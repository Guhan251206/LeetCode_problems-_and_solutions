# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        n=len(a)
        if n<=2:
            return [-1,-1]
        b=[]
        for i in range(1,n-1):
            if (a[i]>a[i-1] and a[i]>a[i+1]) or (a[i]<a[i-1] and a[i]<a[i+1]):
                b.append(i)
        print(b)
        if len(b)<2:
            return [-1,-1]
        max1=b[-1]-b[0]
        min1=b[-1]
        for i in range(len(b)-1):
            if b[i+1]-b[i]<min1:
                min1=b[i+1]-b[i]
        return [min1,max1]