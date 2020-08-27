class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        General idea: use dfs in both directions - from Pacific edge and from Atlantic edge. If the grid cell can be visited from both oceans -> append it to answer.
        1. Base case: empty matrix -> return []
        2. Initialize 2 visited matrixes with Falses. They will store True if the grid cell can be visited from Pacific edge or Atlantic edge respectively.
        3. Iterate through all 4 boarders and start dfs method to fill in visited matrixes
            Dfs method
            1. Make visited True
            2. Iterate through neighboring cells
                1. If the neighboring cell can be accessed (it lies in matrix, it's not in visited and it's values is no less than current) -> start new dfs recursively for that neighboring cell
        4. Use 2 nested loops for matrix. If the grid cell can be visited from both edges (is True) -> append it to answer.
        """
        
        def dfs(x, y, visited):
            visited[x][y] = True
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                if nx >= 0 and nx < m and ny >= 0 and ny < n and not visited[nx][ny] and matrix[nx][ny] >= matrix[x][y]:
                    dfs(nx, ny, visited)
              
        if len(matrix) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        ans = []
        for i in range(m):
            dfs(i, 0, p_visited)
            dfs(i, n-1, a_visited)
        for j in range(n):
            dfs(0, j, p_visited)
            dfs(m-1, j, a_visited)
        
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    ans.append([i,j])
        return ans