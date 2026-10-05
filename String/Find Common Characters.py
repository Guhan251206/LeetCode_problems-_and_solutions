class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        ans=[]
        for x in set(words[0]):
            mini=float('inf')
            for word in words:
                count=0
                for ch in word:
                    if ch==x:
                        count+=1
                mini=min(count,mini)
            for i in range(mini):
                ans.append(x)
        return ans