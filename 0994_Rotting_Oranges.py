class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        General idea: append all rotten oranges to the stack.
        Use BFS and a list called 'new' to update stack after it has been emptied.
        At the end - check if any orange is still fresh (grid[i][j]=1).
        """
        if not grid:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        q = [(i,j) for i in range(rows) for j in range(cols) if grid[i][j] == 2]
        direct = [(-1,0), (1,0), (0,-1), (0,1)]

        time = 0
        while q:
            new = []
            for (x,y) in q:
                for dx, dy in direct:
                    nx, ny = x+dx, y+dy  
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        new.append((nx, ny))  
            q = new
            if q:
                time += 1
                
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return time 
        
