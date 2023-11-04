class Solution(object):
    def lengthOfLastWord(self, s):
        count=0
        flag=False
        for i in range(len(s)-1,-1,-1):
            if(s[i]>='a' and s[i]<='z')or (s[i]>='A' and s[i]<='Z'):
                flag=True
                count+=1
            elif(flag==True):
                return count
        return count
