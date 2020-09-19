class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        General idea: use increasing stack
        1. Initialize empty stack
        2. Iterate through nums
            1. Use while loop to check if last element in stack is larger than current element
                1. Pop from stack
                2. Decrease k
            2. Append current element to stack
        3. Return joined stack, remove first elements if they are zeros. If it will be empty stack -> return '0'. Also about stack[:len(stack)-k]:
        - if stack = [‘9’], k = 1, never decreased, joined stack will be empty string and returned ‘0’
        """
        stack = []
        for x in num:
            while stack and stack[-1] > x and k > 0:
                stack.pop()
                k -= 1
            stack.append(x)
        return ''.join(stack[:len(stack)-k]).lstrip('0') or '0'
        