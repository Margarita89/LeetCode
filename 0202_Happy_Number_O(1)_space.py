class Solution:
    def isHappy(self, n: int) -> bool:
        """
        General idea: use slow and fast pointers (O(1) space). Either fast (2x speed) will reach 1 (1 is cycled to 1) or there is another cycle and fast will reach slow
        1. next_n method to return next n
        2. Initialize slow and fast pointers as n and next_n(n)
        3. Use while loop with slow pointer not equal to fast and fast not equal to 1
            1. Update slow as next to it
            2. Update fast as next next to it (2x speed)
        4. Return fast == 1
        """
        def next_n(n):
            return sum(int(digit)**2 for digit in str(n))
            
        slow, fast = n, next_n(n)
        while slow != fast and fast != 1:
            slow = next_n(slow)
            fast = next_n(next_n(fast))
        return fast == 1