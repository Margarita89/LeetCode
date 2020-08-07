from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        General idea: use dfs from node and it's parent;
        use visited_time and low_time and compare them.
        Important: update low_time recursively from non-parent connection. 
        1. If not visited - perform dfs and then update as min of their low_times
        2. If visited and not parent (cycle) - update low_time as min between low_time and adjacent visited_time
        If adjacent node was not able to get low_time (so it's not in cycle with current node)
        - it's a critical connection.        
        """
        graph = defaultdict(set)
        for v1, v2 in connections:
            graph[v1].add(v2)
            graph[v2].add(v1)
        visited_time = {}
        low_time = {}
        critical = []
        time = 0
        
        def dfs(v, parent):
            nonlocal time
            visited_time[v] = time
            low_time[v] = time
            time += 1
            for u in graph[v]:
                if u not in visited_time:
                    dfs(u, v)
                    low_time[v] = min(low_time[v], low_time[u])
                    # if the neighbor can't get to a lower order node
                    # than your own order -> neighbor link is critical
                    if low_time[u] > visited_time[v]:
                        critical.append([v, u])
                elif u != parent:
                    # because low_time is not yet updated for u
                    low_time[v] = min(low_time[v], visited_time[u])
        
        for v in graph:
            if v not in visited_time:
                dfs(v, None)
        return critical