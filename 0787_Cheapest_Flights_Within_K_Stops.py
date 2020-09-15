from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        General idea: use bfs
        1. Base case: if source is destination -> return 0
        2. Initialize a defaultdict of flights: {source : (destination, price)} and empty dictionary of visited cities to store cheapest prices
        3. Initialize deque 'q' as a list of tuples. Append first tuple: (source, number of cities (distance) = K + 1 and price = 0)
        4. Use while loop for q:
            1. popleft from q a tuple: city, number of cities to visit and price
            2. if city is destination or k == 0 (no more flights allowed) -> continue (maybe it's not yet the cheapest price in visited)
            3. Iterate through neighboring cities:
                1. If already visited and the price is lower -> skip (continue)
                2. Else: -> update price in visited
                    -> append neighboring city to q 
        5. Return price from visited[dst] if there is dst, else -> return -1
        Attention: here cities are calculated, not stops -> K + 1
        """
        if src == dst:
            return 0
        
        f_dict = defaultdict(list)
        visited = {}
        for s, d, p in flights:
            f_dict[s].append((d, p))
        
        q = deque([(src, K + 1, 0)])
        while q:
            city, k, p = q.popleft()
            if city == dst or k == 0:
                continue
            for n_city, p2 in f_dict[city]:
                if n_city in visited and p + p2 > visited[n_city]:
                    continue
                else:
                    visited[n_city] = p + p2
                    q.append((n_city, k-1, p + p2))
        return visited[dst] if dst in visited else -1