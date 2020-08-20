class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        General idea: use middle element and compare to it
        1. Initialize start and end indexes as first and last in the list
        2. Use while loop until the undexes don't swap
            1. Initialize mid as the middle index of start and end
            2. If mid points to target -> return mid
            3. If the element at the mid index is smaller than target -> change start to mid + 1 (as in the sorted list all elements left to mid will be also smaller)
            4. Else: -> change end to mid - 1
        """
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target: 
                return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1