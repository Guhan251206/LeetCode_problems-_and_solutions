class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def fun(a):
            if len(nums)==len(a):
                sol.append(a[:])
                return
            for i in range(len(nums)):
                if ch[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not ch[i-1]:
                    continue
                a.append(nums[i])
                ch[i]=True
                fun(a)
                a.pop()
                ch[i]=False
        sol=[]
        ch=[False]*len(nums)
        fun([])
        return sol