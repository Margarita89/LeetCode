class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        General idea: use rstrip method to remove last spaces, then split, find the last word and return the length
        """
        return len(s.rstrip(' ').split(' ')[-1])
        