class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        General idea: perform multiplication line by line
        1. Iterate through both strings with 2 nested loops
        2. Calculate current product 
        3. Update result using shift 
        4. Return string of result
        """
        res, product = 0, 0
        for i, s2 in enumerate(num2[::-1]):
            for j, s1 in enumerate(num1[::-1]):
                product = int(s1) * int(s2)
                res += product * (10 ** (i + j))
        return str(res)