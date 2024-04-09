class Solution:
    def timeRequiredToBuy(self, t: List[int], k: int) -> int:
        cnt=0
        temp=t[k]
        while t[k]>0:
            
            for i in range(len(t)):
                
                if t[i]>0:
                    
                    cnt+=1
                    t[i]-=1
                    if i==k and t[k]==0:
                        
                        return cnt 
        return cnt