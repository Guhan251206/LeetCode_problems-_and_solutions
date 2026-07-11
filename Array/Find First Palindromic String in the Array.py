class Solution:
    def sortedSquares(self, nums):
        a=[x**2 for x in nums]
        a.sort()
        return a