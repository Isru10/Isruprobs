class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        s=set()
        
        def solve(matrix, i,j):
            for x in range(m):
                if matrix[x][j]==0:
                    continue 
                else:
                    matrix[x][j]=0
                    s.add((x,j))
            for y in range(n):
                if matrix[i][y]==0:
                    continue 
                else:
                    matrix[i][y]=0
                    s.add((i,y))
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0 and (i,j) not in s:
                    solve(matrix,i,j)
        return matrix