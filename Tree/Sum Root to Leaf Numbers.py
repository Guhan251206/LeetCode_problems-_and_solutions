# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=0
        def fun(root,path):
            nonlocal ans
            if not root:
                return 
            path=path*10+root.val
            if not root.left and not root.right:
                ans+=path
            fun(root.left,path)
            fun(root.right,path)
            path=path//10
        fun(root,0)
        return ans