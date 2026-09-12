# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        memo={}
        def dfs(root):
            if not root:
                return 0
            if root in memo:
                return memo[root]
            ans=dfs(root.left)+dfs(root.right)+root.val
            memo[root]=ans
            return ans
        dfs(root)
        memo2={}
        def depth(root):
            if not root:
                return 0
            if root in memo2:
                return memo2[root]
            ans=1+depth(root.left)+depth(root.right)
            memo2[root]=ans
            return ans
        depth(root)
        count=0

        for x in memo:
            if memo[x]//memo2[x]==x.val:
                count+=1
        return count
