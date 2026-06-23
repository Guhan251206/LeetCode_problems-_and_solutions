class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        i=0
        j=len(s)-1
        while i<j:
            if (s[i] in "AEIOUaeiou") and (s[j] in "AEIOUaeiou"):
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i] in "AEIOUaeiou":
                j-=1
            elif s[j] in "AEIOUaeiou":
                i+=1
            else: 
                i+=1
                j-=1
        a="".join(s)
        return a