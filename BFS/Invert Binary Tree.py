# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q=deque()
        dummy=TreeNode(root.val)
        
        q.append((root,dummy))
        while q:
            n=len(q)
            for i in range(n):
                node,t=q.popleft()
                if node.left:
                    t.right=TreeNode(node.left.val)
                    q.append((node.left,t.right))
                if node.right:
                    t.left=TreeNode(node.right.val)
                    q.append((node.right,t.left))
        return dummy