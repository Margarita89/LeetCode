class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        General idea: sliding window with pointer to start of the window
        1. Initialize a hashmap of chars: {ch: last_seen_index}
        2. Initialize pointer 'start' to point to window left border
        3. Iterate through all letters
            - if letter not yet in chars or it's index in chars is outside window ->
            update longest subtring length
            - else -> update 'start' of the window to exclude previously encountered letter
            - update chars with new index (now this letter is encountered only once in the window)
        """
        chars = {}
        longest = start = 0
        for i, ch in enumerate(s):
            if ch not in chars or chars[ch] < start:
                longest = max(longest, i - start + 1)
            else:
                start = chars[ch] + 1
            chars[ch] = i
        return longest
                
        