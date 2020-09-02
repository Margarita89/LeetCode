class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        General idea: find left and right positions using separate Binary Searchs
        """
        def binarySearchLeft(arr, x):
            start, end = 0, len(arr) - 1
            while start <= end:
                mid = (start + end) //2
                if arr[mid] < x:
                    start = mid + 1
                else:
                    end = mid - 1
            return start
        
        def binarySearchRight(arr, x):
            start, end = 0, len(arr) - 1
            while start <= end:
                mid = (start + end) //2
                if arr[mid] <= x:
                    start = mid + 1
                else:
                    end = mid - 1
            return end
        
        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return [left, right] if left <= right else [-1, -1]