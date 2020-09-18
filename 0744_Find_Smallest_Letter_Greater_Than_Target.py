class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        General idea: use binary search and when return check if letters should be wrapped and letters[0] should be returned.
        """
        start, end = 0, len(letters) - 1
        while start <= end:
            mid = (start + end) // 2
            if letters[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        return letters[end + 1] if end + 1 < len(letters) else letters[0]