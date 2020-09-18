class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        General idea: use binary search
        1. start, end - first and last indexes
        2. use while start < end loop
            1. mid is middle index between start and end
            2. if nums[mid] is larger then next element -> it's worth  to consider half with mid and make end = mid
            3. else -> start = mid + 1 as nums[mid] can't be a peak
        3. Return start or end (they are equal when out of while loop)
        """
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid + 1
        return end