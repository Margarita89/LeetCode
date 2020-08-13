class Solution:
    """
    General idea: palindrom can be centered around 1 character or 2.
    Check each character for being central in palindrome or being left to center. 
    1. Method to check for palindrome (accepts starting left and right):
        1. With while loop explore how far left and right pointer can be pushed 
        	to keep palindrome
        2. Return resulting palindrome
    2. Iterate through all letters in s and check if they are the middle of             
    	palindrome (with 1 middle letter or 2) 
    3. Update answer if the length of returned palindrome is larger

    """
    def check_pal(self, s, l, r) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
        
    def update_longest(self, cur, longest) -> str:
        if len(longest) < len(cur):
            longest = cur
        return longest
    
    def longestPalindrome(self, s: str) -> str:
        longest_pal = ''
        for i in range(len(s)):
            cur = self.check_pal(s, i, i) # check with middle in 1 char
            longest_pal = self.update_longest(cur, longest_pal)
            cur = self.check_pal(s, i, i+1) # check with middle in 2 chars    
            longest_pal = self.update_longest(cur, longest_pal)
        return longest_pal