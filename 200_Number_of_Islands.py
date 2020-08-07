from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        General idea: solve with BFS. Replace visited island with counter
        """
        def bfs(i, j, visited, count):
            q = deque()
            q.append((i,j))
            direct = [(-1,0), (1,0), (0,-1), (0,1)]
            
            rows = len(grid)
            cols = len(grid[0])
            while q:
                i, j = q.popleft()
                visited.add((i,j))
                for d in direct:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < rows and 0 <= nj < cols and (ni,nj) not in visited:
                        if grid[ni][nj] == '1':
                            grid[ni][nj] = count
                            q.append((ni,nj))
            
        count = 2
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == '1':
                    bfs(i, j, visited, count)
                    count += 1
        return count - 2
        