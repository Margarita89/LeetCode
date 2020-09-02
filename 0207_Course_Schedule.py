from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        General idea: use dfs and try to check if there are cycles
        1. Create a list of colors (0 - not visited, 1 - in process, 2 - finished)
        2. Use defaultdict to store prerequisites
        3. For all courses that have color = 0 start dfs
        4. Dfs:
            1. Change color to 1
            2. Iterate through all prerequisites
                1. If color is 0 -> start dfs and return False if it returns False
                2. Elif color is 1 -> it's a cycle detected (not parent, but also not finished yet) -> return False
            3. Make color = 2 - finished
            4. Return True
        """   
        def dfs(v, color, dicty):
            color[v] = 1
            for u in dicty[v]:
                if color[u] == 0:
                     if not dfs(u, color, dicty):
                        return False
                elif color[u] == 1:
                    return False
            color[v] = 2
            return True
        
        
        color = [0] * numCourses
        dicty = defaultdict(list)
        for p in prerequisites:
            dicty[p[1]].append(p[0])
        for i in range(numCourses):
            if color[i] == 0:
                if not dfs(i, color, dicty):
                    return False
        return True
        
        