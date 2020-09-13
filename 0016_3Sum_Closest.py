class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        General idea: use 2 pointers (start and end) to find a sum of 2 in sorted array
        1. Initialize min_diff as maximum 
        2. Sort array of nums
        3. Iterate through array of nums (except 2 last elements)
            1. Initialize 2 pointers to find sum of 2 (start and end of the rest of nums)
            2. Use while loop for the pointers
                1. Initialize cur_sum as a sum of 3
                2. if this sum is closer to target -> update min_diff
                3. if this sum is smaller than target -> move start index
                4. else -> move end index
            3. if min_diff is 0, it means sum of 3 is equal to target -> break (no need to continue). Maybe here can be just return target
        4. Return the difference between target and min_diff
        """
        min_diff = float('inf')
        nums.sort()
        for i in range(len(nums) - 2):
            j, k  = i + 1, len(nums) - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if abs(min_diff) > abs(target - cur_sum):
                    min_diff = target - cur_sum
                if cur_sum < target:
                    j += 1
                else:
                    k -= 1
            if min_diff == 0:
                break
        return target - min_diff