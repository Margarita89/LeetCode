class Solution:
    def reverseBits(self, n: int) -> int:
        """
        General idea: use mask to get the right bit equal to 1 in n. Then add this bit in a power of (32 - i - 1) to the answer
        1. Initialize answer as 0
        2. Iterate through 32 bits in n
            1. Create a mask as bit on ith position, ex: 1000 when i = 3
            2. If mask applied to n will find a bit:
                1. Add this bit to answer in a power of (32 - i - 1)
        3. Return answer
        """
        ans = 0
        for i in range(32):
            mask = 1 << i
            if mask & n:
                ans = ans | (1 << (32 - i - 1))
        return ans