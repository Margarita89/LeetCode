class Solution:
    def rotatedDigits(self, N: int) -> int:
        """
        General idea: use helping function to check if current number rotates to different number and isubset method
        1. Initialize 2 sets: one with digits that rotate to themselves and another with digits that a valid after rotation
        2. Helping function: good_rotated from string
            1. Create a set of digits from string
            2. Return checking if current set is subset of valid set of digits and not subset of set with digits rotating to themselves. The last condition is important: if the current set would be a subset of digits rotating to themselves -> the number will be the same
        3. Return sum through all numbers from 1 to N + 1
        """
        def good_rotated(k):
            set_check = {int(i) for i in k}
            return set_check.issubset(set_valid) and not set_check.issubset(set_themselves)
        
        set_themselves = {0, 1, 8}
        set_valid = {0, 1, 2, 5, 6, 8, 9}
        return sum(good_rotated(str(i)) for i in range(1, N + 1))