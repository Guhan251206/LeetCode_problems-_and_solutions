class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            ind=word.index(ch)
            s=word[:ind+1]
            return s[::-1]+word[ind+1:]
        else:
            return word
        