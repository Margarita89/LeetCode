class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        General idea: substract divisor multiplied by a counter from dividend. Counter is doubled each time. If it's impossible to substract more (will lead to negative dividend) just start from beginning 1 divisor, 2 divisors and so on. Can be done without multiplication at all -> refactor
        1. Save the resulting sign and use only abs values from dividend and divisor
        2. Initialize res as zero
        3. Use while loop to check if it's worth further decreasing dividend
            1. Initialize count_divisor as 1
            2. Use while loop to check if dividend can be further decreased using updated divisor
                1. Update res adding a count_divisor (how many times divisor is subtracted from dividend)
                2. Decrease divident
                3. Updated count_divisor by doubing it
        4. Return res * sign if it's within limits => else: return one of the limits
        """
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            count_divisor = 1
            while dividend >= divisor * count_divisor:
                res += count_divisor
                dividend -= divisor * count_divisor
                count_divisor += count_divisor
        if res * sign <= 2**31 -1 and res * sign >= - 2 **31:
            return res* sign
        if res * sign > 2**31 -1:
            return 2**31 -1
        return - 2 **31