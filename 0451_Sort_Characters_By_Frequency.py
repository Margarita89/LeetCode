from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        """
        General idea: use counter
        1. Use Counter dictionary to calculate characters' frequencies
        2. Transfer dictionary to list
        3. Sort list in decreasing order
        4. Use join to return correct answer
        """
        count_s = Counter(s)
        list_s = [(x, val) for x, val in count_s.items()]
        list_s.sort(key=lambda x: -x[1])
        return ''.join(map(str, [ch * val for ch, val in list_s]))