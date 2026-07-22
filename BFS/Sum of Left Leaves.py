# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque()
        d=0
        q.append(root)
        while q:
            n=len(q)
            for i in range(n):
                node=q.popleft()
                if node.left:
                    if not node.left.left and not node.left.right:
                        d+=node.left.val
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return d