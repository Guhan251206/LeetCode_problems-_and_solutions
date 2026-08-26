class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l=0
        ones=0
        ans=''
        for r in range(len(s)):
            if s[r]=='1':
                ones+=1
            while ones>k:
                if s[l]=='1':
                    ones-=1
                l+=1
            if k==ones:
                while l<r and s[l]=='0':
                    l+=1
                cur=s[l:r+1]
                if not ans or len(ans)>len(cur) or (len(cur)==len(ans) and cur<ans):
                    ans=cur
      
        return ans