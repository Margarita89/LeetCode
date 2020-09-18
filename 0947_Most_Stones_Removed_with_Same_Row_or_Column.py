from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        General idea: use graph which will store stones that share a column or a row as connected to together by refering to their indexes in stones. Then use dfs or bfs to calculate the number of move
        1. Initialize a graph and store all stones that share a column or a row by their indexes
        2. Initialize ans = 0 and a list 'visited' with all False to check if the stone was moved
        3. Iterate through stones
            1. If the stone was not visited ->
                1. Inialize a list q with this stone and make visited True
                2. Use while loop for this list q until empty
                    1. Pop last stone from q and increase ans
                    2. Iterate through its' neightbors in the graph and if they are not yet visited -> append to q, make visited True
                3. Decrease ans by 1 (so in total only nodes - 1 can be moved in 1 component)
        4. Return ans
        """
        graph = defaultdict(list)
        for i, stone1 in enumerate(stones):
            for j in range(i):
                stone2 = stones[j]
                if stone1[0] == stone2[0] or stone1[1] == stone2[1]:
                    graph[i].append(j)
                    graph[j].append(i)
        n = len(stones)
        ans = 0
        
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                q = [i]
                visited[i] = True
                while q:
                    node = q.pop()
                    ans += 1
                    for nei in graph[node]:
                        if not visited[nei]:
                            q.append(nei)
                            visited[nei] = True
                ans -= 1
        return ans