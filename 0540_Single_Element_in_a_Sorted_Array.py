class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        General idea: use binary search and check for the middle element if it's neighbor lie where expected (on the right or on the left depending on if middle is even or odd)
        """
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if mid % 2 == 0 and nums[mid] != nums[mid + 1]:
                if nums[mid] != nums[mid - 1]:
                    return nums[mid]
                end = mid - 1
            elif mid % 2 == 1 and nums[mid] != nums[mid - 1]:
                if nums[mid] != nums[mid + 1]:
                    return nums[mid]
                end = mid - 1
            else:
                start = mid + 1
        return nums[start]
                