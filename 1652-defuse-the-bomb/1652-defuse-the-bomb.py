class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        output=[]
        for i in range(len(code)):
            if k>0:
                j=i+1
                m=k
                sum=0
                while m :
                    sum+=code[j%len(code)]
                    m-=1
                    j+=1
                output.append(sum)
            elif k==0:
                output.append(0)
            else:
                j=i-1
                m=k
                sum=0
                while m :
                    sum+=code[j%len(code)]
                    m+=1
                    j-=1
                output.append(sum)
        return output
                    
                    
            