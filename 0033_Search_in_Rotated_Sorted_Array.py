class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        General idea: find an index where the list is separated
        1. Check if list of nums is empty -> return -1
        2. Use binary search to find an index where the list is separated
        3. Initialize l, r - start and end indexes for where target might be located
        4. Use binary search and return the index if it exists
        """
        if not nums:
            return -1
    
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] > nums[0]:
                l = mid
            else:
                r = mid
        ind = r # where nums is separated
    
        if nums[0] <= target <= nums[ind - 1]:
            l, r = 0, ind - 1 
        elif nums[ind] <= target <= nums[-1]:
            l, r = ind, len(nums) - 1
        else:
            return -1
                
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid

        if nums[l] == target: return l
        if nums[r] == target: return r
        return -1