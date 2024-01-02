class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        used = [False]* n
        
        
        def traverse(start ):
            q=collections.deque()
            q.append(start)
            used[start]=True
            while len(q)>0:
                current=q.popleft()
                for i in range(n):
                    if isConnected [current][i] and not used[i]:
                        q.append(i)
                        used[i]=True
                        
        
        province=0
        for i in range(n):
            if not used[i]:
                province+=1
                traverse(i)
        return province
    