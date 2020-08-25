class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        General idea: sort array, iteratively choose negative first element and then use 2 pointers (from start and end) to find 2 other elements.
        1. Sort array of nums
        2. Initialize array of answers
        3. Iterate through elements of nums (from first till the last-2 to allow 2 elements to be chosen)
            1. If the element is positive - break (there should be at least 1 negative element to sum to zero and as the array is sorted, at least first element should be negative)
            2. Check if the previous element is the same -> continue to avoid repetitions
            3. Use 2 pointers approach for the next 2 elements on the rest of array
                1. Initialize cur_sum as a sum of 3 elements
                2. If cur_sum is zero - append all 3 elements to answer and move left and right pointers
                3. If cur_sum is not zero - move left or right pointers
        4. Return answer
        """
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if cur_sum == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif cur_sum > 0:
                    r -= 1
                else:
                    l += 1
        return ans
                    
        