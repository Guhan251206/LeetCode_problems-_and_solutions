from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], t: int) -> bool:
        if not root:
            return False
        q=deque()
        q.append((root,t-root.val))
        sum=0
        while q:
            node,sum=q.popleft()
            if not node.left and not node.right and sum==0:
                return True
            if node.left:
                q.append((node.left,sum-node.left.val))
            if node.right:
                q.append((node.right,sum-node.right.val))
        return False