# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        def fun(root):
            if root:
                fun(root.left)
                a.append(root.val)
                fun(root.right)
            return a
        return fun(root)