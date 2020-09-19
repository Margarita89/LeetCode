class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        General idea: use dictionary to store how many times each sum from start of array occured. Then use the idea: sum_x - sum_y = k -> then subarray between y and x has a sum of k. So, it makes sense to check how many times sum_x - k was encountered and it will be how many times sum k was encountered.
        1. Initialize dictionary prefix_sum as 0: 1 as it will be useful when the current sum will be equal to k 
        2. Initialize result 'res' as 0 and current sum 'cur_sum' as 0
        3. Iterate through nums
            1. Update current sum
            2. Update res by adding a value from prefix_sum for current sum - k (or 0 if it's not there)
            3. Update counter for prefix_sum[cur_sum]
        4. Return res
        """
        prefix_sum = {0 : 1}
        res, cur_sum = 0, 0
        for num in nums:
            cur_sum += num
            res += prefix_sum.get(cur_sum - k, 0)
            prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1
        return res
        560. Subarray Sum Equals K