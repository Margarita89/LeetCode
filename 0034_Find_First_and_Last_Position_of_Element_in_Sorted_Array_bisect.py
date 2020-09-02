import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        General idea: use bisect_left and bisect to find left and right positions. Don't forget to substract 1 from the result of bisect for right position
        """        
        left, right = bisect.bisect_left(nums, target), bisect.bisect(nums, target) - 1
        return [left, right] if left <= right else [-1, -1]