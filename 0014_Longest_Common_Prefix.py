class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        General idea: find min and max (lexigraphical order) in a list of strs and iterate through min comparing it to max.
        1. Find min and max strings in strs according to lexigraphical order
        2. Iterate through min string and compare each character to corresponding in max string. 
            1. If they are not equal – return min string[:i] 
        3. Return min string (it itself is a longest common prefix)
        """
        if not strs:
            return ''
        s1 = min(strs)  # min lexigraphical order
        s2 = max(strs)  # max lexigraphical order
        for i, ch in enumerate(s1):
            if ch != s2[i]:
                return s1[:i]
        return s1
        