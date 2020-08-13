from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        1. Put all zeros into deque: tuple with their coordinates and distance = 0
        2. Create a set with coordinates of visited cells
        3. Create a list of 0's that will be filled with resulting distances
        4. BFS updating answering list with distances
        5. Don't forget to add to the visited set
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        q = deque([(r,c,0) 
                   for r in range(rows) 
                   for c in range(cols) 
                   if matrix[r][c] == 0])
        
        visited = {(x,y) for x,y,_ in q}
        ans = [[0 for _ in range(cols)] for _ in range(rows)]
            
        direct = [(0,-1), (0,1), (-1,0), (1,0)]
        while q:
            x, y, count = q.popleft()
            ans[x][y] = count
            for d in direct:
                nx, ny = x+d[0], y+d[1]
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:        
                    q.append((nx,ny,count+1))
                    visited.add((nx,ny))
       
        return ans
    
    
