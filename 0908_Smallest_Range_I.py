class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        """
        General idea: it's required to decrease difference between max(A) and min(A) and it's possible to do it by substracting maximum K from each of them. It can also make result negative which is not desirable, so -> use max(0, ..)
        """
        return max(max(A) - min(A) - 2 * K, 0)