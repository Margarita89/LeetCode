from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        General idea: use Counter and then compare amount of distinct number pccurences using set
        """
        counter_numbers = Counter(arr)
        return len(counter_numbers.values()) == len(set(counter_numbers.values()))