class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        General idea: use sliding window
        1. Create 'char_p' with Counter for p: {character: frequency}
        2. Initialize l and r pointers for window starting at 0's
        3. Initialize counter - number of different characters in p
        4. Use while loop with r pointer
            1. If character is in 'char_p' of t -> decrease it's frequency and if there are no such characters in 'char_p' -> decrease counter
            2. Increase r
            3. While counter is 0 (which means all characters in p are included in window)
                1. Update start_indexes if needed
                2. Update 'char_p' if character from left border is in p and update counter if this character is first time in 'char_p'
                3. Increase l
        5. Return start_indexes
        """
        chars_p = collections.Counter(p)
        counter = len(chars_p)
        l, r, start_indexes = 0, 0, []
        
        while r < len(s):
            if s[r] in chars_p:
                chars_p[s[r]] -= 1
                if chars_p[s[r]] == 0:
                    counter -= 1
            r += 1
            
            while counter == 0:
                if r - l == len(p):
                    start_indexes.append(l)
                if s[l] in chars_p:
                    chars_p[s[l]] += 1
                    if chars_p[s[l]] == 1:
                        counter += 1
                l += 1
        
        return start_indexes
        