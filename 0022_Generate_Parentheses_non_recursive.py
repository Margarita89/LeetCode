class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        General idea: use bfs method.
        1. Base case: n is 0 -> return list with empty string
        2. Initialize deque with a pair of parentheses: '()' and decrease n
        3. Use while loop for n > 0
            1. Initialize tmp set to store new parentheses
            2. Use while loop to empty q
                1. Pop first parentheses from q
                2. Iterate through them and add pair of parentheses: '()' at every place and store result each time into tmp set (which allows to avoid repetitions)
            3. Make q equal to tmp and decrease n
        4. Return q (now it has all combinations of different n pairs of parentheses)
        """
        if n == 0:
            return ['']
        
        q = deque(['()'])
        n -= 1
        while n > 0:
            tmp = set()
            while q:
                cur = q.popleft()
                for i, ch in enumerate(cur):
                    tmp.add(cur[:i] + '()' + cur[i:])
            q = deque(tmp)
            n -= 1
        return q