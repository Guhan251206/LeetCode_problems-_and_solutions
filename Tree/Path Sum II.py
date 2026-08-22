# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], t: int) -> List[List[int]]:
        ans=[]
        def fun(root,path,total):
            nonlocal ans
            if not root:
                return
            path.append(root.val)
            total+=root.val
            if not root.left and not root.right:
                if total==t:
                    ans.append(path.copy())
            else:
                fun(root.left,path,total)
                fun(root.right,path,total)
            path.pop()
            
            
        fun(root,[],0)
        return ans