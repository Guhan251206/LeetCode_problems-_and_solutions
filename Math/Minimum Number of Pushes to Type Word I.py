class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt=0
        c=1
        for i in range(len(word)):
            cnt+=c
            if (i+1)%8==0:
                c+=1
        return cnt