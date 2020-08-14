class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        General idea: use recursion with left and right as a number of open and closed parentheses
        1. Base case: length of s is equal to 2*n - means all parentheses are included -> append to answer
        2. If number of left parentheses is less than half (which is n) -> add '(' and start over
        3. If number of left parentheses is larger than right - it's possible to close -> add ')' and start over
        Thus it will be always <= n opened paranthesis and all combination will be checked
        """
        parentheses = []
        def recursive_parentesis(s, left, right):
            if len(s) == 2 * n:
                parentheses.append(s)
                return
            if left < n:
                recursive_parentesis(s + '(', left + 1, right)
            if left > right:
                recursive_parentesis(s + ')', left, right + 1)
            
        recursive_parentesis('', 0, 0)
        return parentheses