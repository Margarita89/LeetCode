class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        General idea: use sliding window
        1. Create hashmap 'char_t' with Counter for t: {character: frequency}
        2. Initialize l and r pointers for window starting at 0's
        3. Initialize counter - different characters of t
        4. Use while loop with r pointer
            1. If character is in 'char_t' of t -> decrease it's frequency and if there are no such characters in 'char_t' -> decrease counter
            2. Increase r
            3. While counter is 0 (which means all characters in t are included in window)
                1. Update min_window if needed
                2. Update 'char_t' if character from left border is in t and update counter if this character if first time in 'char_t'
                3. Increase l
        5. Return min_window
        """
        
        chars_t = collections.Counter(t)
        counter = len(chars_t)
        l, r, min_len = 0, 0, float('inf')
        min_window = ''
        
        while r < len(s):
            ch = s[r]
            if ch in chars_t:
                chars_t[ch] -= 1
                if chars_t[ch] == 0:
                    counter -= 1        
            r += 1
            
            while counter == 0:
                if r - l < min_len:  # it's time to update min_len
                    min_len = r - l
                    min_window = s[l:r]
                
                ch = s[l]
                if ch in chars_t:
                    chars_t[ch] += 1
                    if chars_t[ch] == 1:
                        counter += 1
                l += 1
        return min_window
            
                    
        