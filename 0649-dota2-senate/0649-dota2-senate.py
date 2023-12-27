class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        br=0
        bd=0
        cr=0
        cd=0
        tbr=0
        tbd=0
        for sen in senate:
            if sen=='R':
                cr+=1
            else:
                cd+=1
        queue=deque(senate)
        while (queue):
            sen=queue.popleft()
            if sen =='R':
                if br>0:
                    br-=1
                else:
                    bd+=1
                    tbd+=1
                    queue.append(sen)
            else:
                if bd>0:
                    bd-=1
                else:
                    br+=1
                    tbr+=1
                    queue.append(sen)
            if tbd>cd:
                return 'Radiant'
            elif tbr>cr:
                return 'Dire'
        return -1