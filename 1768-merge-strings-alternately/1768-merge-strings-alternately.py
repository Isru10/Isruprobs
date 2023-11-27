class Solution(object):
    def mergeAlternately(self, word1, word2):
        i=0
        l=[]
        while i<len (word1) or i<len(word2):
                if i<len(word1):
                    l.append(word1[i])
                if i<len(word2):
                    l.append(word2[i])
                i+=1
                
        return ''.join(l )
              

      

        
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        