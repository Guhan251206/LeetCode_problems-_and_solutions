class Solution:
    def getPermutation(self, n: int, k: int):
        def fun(nums, a):
            nonlocal cnt, ans

            if ans:          
                return

            if len(a) == len(nums):
                cnt += 1
                if cnt == k:
                    ans = "".join(map(str, a))
                return

            for i in range(len(nums)):
                if vis[i]:
                    continue

                vis[i] = True
                a.append(nums[i])
                fun(nums, a)
                a.pop()
                vis[i] = False

                if ans:      
                    return

        nums = [i for i in range(1, n + 1)]
        vis = [False] * n
        cnt = 0
        ans = ""

        fun(nums, [])
        return ans