class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        n=list(set(nums))
        n.sort()
        if len(n)>2:
            return n[len(n)-3]
        else:
            return max(nums)