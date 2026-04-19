from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        perimeter=0
        visit=set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:   
                     # Start BFS only when we find the island
                    q=deque([(r,c)])
                    visit.add((r,c)) # necessary to add the first r,c to visit set manually

                    while q:
                        r,c = q.popleft()
                        directions = [[1,0],[-1,0],[0,1],[0,-1]]

                        for dr,dc in directions:
                            nr,nc = r+dr, c+dc

                             # 1. If neighbor is out of bounds or water -> +1 Perimeter
                            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                                perimeter += 1

                            elif (nr, nc) not in visit:
                                visit.add((nr,nc))
                                q.append((nr,nc))
                    return perimeter                             

                        


                
    