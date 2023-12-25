class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cs=grid[0]
        c=[[] for _ in cs]
        for row in grid :
            for j, element in enumerate (row):
                c[j].append(element)
        ep=0
        for row in grid :
            for j, element in enumerate (cs):
                if row[0]==element:
                    if row == c[j]:
                        ep+=1
        return ep