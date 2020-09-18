class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """
        General idea: sort array and find minimum difference, after that append all pairs of elements with this difference
        """
        arr.sort()
        min_diff = float('inf')
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] < min_diff:
                min_diff = arr[i] - arr[i-1]
        min_differences = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                min_differences.append([arr[i-1], arr[i]])
        return min_differences