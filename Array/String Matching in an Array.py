class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        a=[]
        for i in words:
            for j in range(len(words)):
                if (i!=words[j]) and (i in words[j] ):
                    a.append(i)
                    break
        return a