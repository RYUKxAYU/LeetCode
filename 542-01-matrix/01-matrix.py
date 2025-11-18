from collections import deque 
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        
        dis = [[-1] * col for _ in range(row)] 
        queue = deque()
        
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    dis[r][c] = 0
                    queue.append((r, c))

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] 
        while queue:
            curr_row, curr_col = queue.popleft() 
            
            for row_offset, col_offset in directions:
                next_row = curr_row + row_offset
                next_col = curr_col + col_offset

                if 0 <= next_row < row and 0 <= next_col < col and dis[next_row][next_col] == -1:
                    dis[next_row][next_col] = dis[curr_row][curr_col] + 1
                    queue.append((next_row, next_col))
                    
        return dis 