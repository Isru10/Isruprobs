class Solution:
    def leastInterval(self, task: List[str], n: int) -> int:
        if not task :
            return 0
        freq=Counter(task)
        sortedfreq=sorted(freq.values(),reverse=True)

        chunk=sortedfreq[0]-1
        idle=chunk*n
        for f in sortedfreq[1:]:
            idle-=min(chunk,f)
        return len(task) if idle<0 else idle+len(task)