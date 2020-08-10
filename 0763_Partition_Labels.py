class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        """
        1. Create a dictionary {ch: ind}, where 'ind' is the last encountered index of letter 'ch'
        2. Iterate through string S 
        3. Keep 'end' updated as the last repeated index of the current substring
        4. If end is equal to current index, then all letters of current substring 
            appear only in that substring
        5. Don't forget to update 'start'
        """
        if len(S) == 0:
            return [0]
        
        last_ind = {}
        for ind, ch in enumerate(S):
            last_ind[ch] = ind
        
        start, end = 0, 0
        ans = []
        for ind, ch in enumerate(S):
            end = max(end, last_ind[ch])
            if ind == end:
                ans.append(ind - start + 1) 
                start = ind + 1
        return ans
        