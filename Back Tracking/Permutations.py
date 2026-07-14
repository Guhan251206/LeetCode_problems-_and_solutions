class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def fun(nums,a,sol):
            if len(a)==len(nums):
                sol.append(a[:])
                return
        
            for i in range(len(nums)):
                if nums[i] in a:
                    continue
                a.append(nums[i])
                fun(nums,a,sol)
                a.pop()
        sol=[]
        fun(nums,[],sol)
        return sol