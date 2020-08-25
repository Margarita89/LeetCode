class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        General idea: find where the array is rotated (where max meets min)
        1. Base case: there is no rotation or only 1 element
        2. Use binary search always comparing to first element as in this case all elements before the point of rotation are larger than first element and all elements after the point of rotation are smaller than first element
        """
        
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]
        
        l, r = 0, len(nums) -1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] > nums[0]:
                l = mid 
            else:
                r = mid
        return nums[r]
