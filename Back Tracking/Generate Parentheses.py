class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def fun(path,open,close):
            nonlocal ans
            if open==n and close==n:
                ans.append("".join(path))
                return
            if open<n:
                fun(path+'(',open+1,close)
            if close<open:
                fun(path+')',open,close+1)
        fun("",0,0)
        return ans