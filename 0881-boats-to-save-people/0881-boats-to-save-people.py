class Solution:
    def numRescueBoats(self, ppl: List[int], lim: int) -> int:
        ppl.sort()
        r=len(ppl)-1
        l=0
        cnt=0
        aux=[]
        while l<=r:
            if l==r:
                if 2*ppl[r]<=lim:
                    aux.append(ppl[l])
                    cnt+=1
                break
            if ppl[l]+ppl[r] <=lim:
                aux.append(ppl[l])
                aux.append(ppl[r])
                r-=1
                l+=1
                cnt+=1
            elif ppl[l]+ppl[r] >lim:
                r-=1

            else:
                break
        return cnt+ len(ppl)-len(aux)