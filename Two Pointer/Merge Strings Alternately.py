class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=j=0
        a=''
        while i<len(word1) or j<len(word2):
            if i<len(word1):
                a+=word1[i]
                i+=1
            if j<len(word2):
                a+=word2[j]
                j+=1
        return a
        