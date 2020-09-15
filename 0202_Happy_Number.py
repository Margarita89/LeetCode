class Solution:
    def isHappy(self, n: int) -> bool:
        """
        General idea: use a hash set to capture the cycle
        1. Initialize empty hash set
        2. Use while loop for n is not equal to 1 and n not in hash set
            1. Add n to hash set
            2. Update n as a sum of square digits
        3. Return n == 1 
        """
        hash_nums = set()
        while n != 1 and not n in hash_nums:
            hash_nums.add(n)
            n = sum(int(digit)**2 for digit in str(n))
        return n == 1