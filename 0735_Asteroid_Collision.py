class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        General idea: use stack to store asteroids
        1. Initialize empty stack
        2. Iterate through asteroids
            1. With while loop check if current astroid moves left and previous in stack moves right (this is only condition to collide)
                1. Check if last is smaller -> pop it and continue to the next
                2. Check if last is the same size -> pop it and break (as current astroid will explode also)
                3. Break. Thus, only first 'if' will be continued
            2. In other case -> append asteroid to stack
        3. Return stack
        """
        
        stack = []
        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:  # only case of meeting
                if stack[-1] < abs(ast):
                    stack.pop()
                    continue
                elif stack[-1] == abs(ast):
                    stack.pop()
                break
            else:
                stack.append(ast)
        return stack