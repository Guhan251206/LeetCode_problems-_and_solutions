# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, t: Optional[TreeNode]) -> int:
        best=float('-inf')
        def dfs(root):
            nonlocal best
            if not root:
                return 0
            l=max(0,dfs(root.left))
            r=max(0,dfs(root.right))
            cur=l+root.val+r
            best=max(best,cur)
            return root.val+max(l,r)
        dfs(t)
        return best
