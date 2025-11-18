from collections import deque  # FIX 1: collections (plural)
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        
        # Initialize distance matrix with -1 (acting as "unvisited")
        dis = [[-1] * col for _ in range(row)] # FIX 2: for _ (space needed)
        queue = deque()
        
        # Step 1: Add all 0s to queue and set their distance to 0
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    dis[r][c] = 0
                    queue.append((r, c))
        
        # Directions: Up, Down, Left, Right
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # Renamed to avoid confusion
        
        # Step 2: BFS
        while queue:
            curr_row, curr_col = queue.popleft() # FIX 3: .popleft()
            
            for row_offset, col_offset in directions: # FIX 4: removed "in dis"
                next_row = curr_row + row_offset
                next_col = curr_col + col_offset
                
                # Check boundaries using 'row' and 'col' (dimensions), not 'r'/'c'
                # Check if the neighbor is unvisited (-1)
                if 0 <= next_row < row and 0 <= next_col < col and dis[next_row][next_col] == -1:
                    dis[next_row][next_col] = dis[curr_row][curr_col] + 1
                    queue.append((next_row, next_col))
                    
        return dis # FIX 5: Return the grid 'dis', not the directions list