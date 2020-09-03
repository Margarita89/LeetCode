class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        General idea: use recursion and check for 2 options with "*" - zero or non zero matches
        1. Base case: pattern p is over -> check if s is also over
        2. Boolean first_match True if is not yet empty and there is a match with p
        3. If there is '*':
            1. Either s matches zero times with p[0], then simply skip s[0:2] -> self.isMatch(s, p[2:])
            2. Or there is a match with first characters and possibly with others from s -> self.isMatch(s[1:], p)
        4. Else if first characters match -> move to the next in s and p
        """
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}
        
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)

        else:
            return first_match and self.isMatch(s[1:], p[1:])