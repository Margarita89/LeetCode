from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        General idea: use Counter to calculate all frequencies. Transfer obtained dictionary into list, sort and return first k values
        """
        count_elements = Counter(nums)
        elem_freq = []
        for key, value in count_elements.items():
            elem_freq.append([key, value])
        elem_freq.sort(key=lambda x: -x[1])
        return [x[0] for x in elem_freq[:k]]