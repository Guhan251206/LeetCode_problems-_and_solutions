class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dict={}
        for k,w in knowledge:
            dict[k]=w
        #print(dict)
        def fun(i):
            r=''
            while i<len(s) and s[i]!=')':
                r+=s[i]
                i+=1
            return r,i+1
        i=0
        ans=''
        while i<len(s):
            if s[i]=='(':
                r,i=fun(i+1)
               # print(r)
                ans+=dict.get(r,'?')
            elif i<len(s):
                ans+=s[i]
                i+=1
        return ans
                