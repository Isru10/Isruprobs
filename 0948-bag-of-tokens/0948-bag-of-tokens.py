class Solution:
    def bagOfTokensScore(self, tokens: List[int], p: int) -> int:
        q=deque(sorted(tokens))
        maxs=0
        sc=0
        while q :
            if p>=q[0]:
                t=q.popleft()
                p-=t
                sc+=1
                maxs=max(maxs, sc)
            elif sc>0:
                t=q.pop()
                p+=t
                sc-=1
            else:
                break
        return maxs