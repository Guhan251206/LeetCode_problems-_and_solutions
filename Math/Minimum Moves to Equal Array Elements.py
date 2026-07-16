class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=min(nums)
        s=0
        for i in nums:
            s+=i-m
        return s