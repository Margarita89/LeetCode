class Solution:
    """
    @param s: a string
    @return: the length of the longest substring T that contains at most 2 distinct characters
    """
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        General idea: sliding window, use a method to calculate at most 
            K distinct characters. Use 2 pointers for the left and right 
            borders of the window and a hashmap to control the number of 
            occurrences of each letter
        1. Initialize a lookup defaultdict to store the number of times 
            each letter was encountered in current window [l, r]
        2. Initialize l, r - 2 pointers for the window
        3. Initialize counter and max_substring (to store results)
        4. Traverse s with while loop for r pointer
            1. Update lookup for the letter s[r]
            2. Update counter if the letter s[r] is first time in lookup 
                - so we know how many different letters we have
            3. Increase r
            4. With while loop move left border of the window to be sure 
                that counter doesn't exceed K
                1. Decrease value of s[l] in lookup
                2. Decrease counter if there are no more s[l] in lookup
                3. Increase l
            5. Update max_substring with the difference (r-l) - it's the number 
                of substrings with at most K different characters 
        5. Return max_substring
        """
        k = 2
        lookup = collections.defaultdict(int)
        l, r, count, max_substring = 0, 0, 0, 0
        while r < len(s):
            lookup[s[r]] += 1
            if lookup[s[r]] == 1:
                count += 1
            r += 1
            while l < r and count > k:
                lookup[s[l]] -= 1
                if lookup[s[l]] == 0:
                    count -= 1
                l += 1
            max_substring = max(max_substring, r - l)
        return max_substring