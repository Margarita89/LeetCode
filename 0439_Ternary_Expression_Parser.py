class Solution:
    """
    @param expression: a string, denote the ternary expression
    @return: a string
    """
    def parseTernary(self, expression):
        """
        1. Check if expression is empty -> return empty string
        2. Compress method (using the idea of ternary expression):
            1. Let string be a slice from expression of size 2 (using index, ex: 'F?') and 3 last popped values from stack
            2. If 1st char string is 'F' -> return 5th char
               ex: 'F?1:3' -> returns 3
            3. In other case -> return 3rd char
               ex: 'T?1:3' -> returns 1
        3. With while loop iterate from the end of expression
            1. Use compress method while possible (starting at expression[ind] == '?')
            2. Append to stack results of compress method and ':'
        4. Return stack[0]
        """
        if not expression:
            return ''
            
        def compress(expression, stack, ind):
            string = expression[ind-1: ind+1] + stack.pop() + stack.pop() + stack.pop() 
            if string[0] == 'F':
                return string[4]
            return string[2]
                
    
        stack = []
        ind = len(expression) - 1
        while ind >= 0:
            while ind >= 1 and len(stack) > 1 and stack[-2] == ':' and expression[ind] == '?':
                compressed = compress(expression, stack, ind)
                stack.append(compressed)
                ind -= 2
            if ind >= 0:
                stack.append(expression[ind])
                ind -= 1
        
        return stack[0]