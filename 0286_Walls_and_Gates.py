from collections import deque
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        """
        1. Iterate through all cells with 2 nested loops
        2. If it's a gate (value is 0) - start bfs
        3. In bfs use a deque with coordinates of a cell and 
            a set with visited cells
        4. Update value in adjacent cells and append them to deque
        """
        def bfs(i,j,rooms):
            count = 1
            q = deque([(i, j, count)])
            direct = [(0,1), (0,-1), (-1,0), (1,0)]
            visited = {(i,j)}
            
            while q:
                x, y, count = q.popleft()
                for (dx, dy) in direct:
                    
                    if 0 <= (x+dx) < rows and 0 <= (y+dy) < cols and \
                        rooms[x+dx][y+dy] > 0 and (x+dx, y+dy) not in visited:
                        
                        rooms[x+dx][y+dy] = min(rooms[x+dx][y+dy], count)
                        q.append((x+dx,y+dy, count+1))
                        visited.add((x+dx,y+dy))
            
        
        rows, cols = len(rooms), len(rooms[0])
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    bfs(i, j, rooms)
            
