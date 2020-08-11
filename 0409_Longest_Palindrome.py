class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        General idea: use Counter and check if each letter 
            occurs odd or even number of times
        """
        count = collections.Counter(s)
        longest_palindrome, odd = 0, 0 
        for ch in count:
            if count[ch] % 2 == 0:
                longest_palindrome += count[ch]
            else:
                odd = 1
                longest_palindrome += count[ch] - 1
        return longest_palindrome if odd == 0 else longest_palindrome + 1