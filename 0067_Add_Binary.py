class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        General idea: use 2 separate methods to convert from decimal to binary and visa versa
        """
        def bin2digit(a):
            ans = 0
            for i, ch in enumerate(a):
                if ch == '1':
                    ans += 2 ** (len(a) - i - 1)
            return ans
        
        def dec2bin(c, ans):
            if c > 1:
                dec2bin(c // 2, ans)
            ans.append(c % 2)
            return ans
        
        sum_digit = bin2digit(a) + bin2digit(b)
        ans = dec2bin(sum_digit, [])
        return ''.join(map(str, ans))