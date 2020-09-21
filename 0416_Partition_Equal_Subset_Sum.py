class Solution:
    def canPartition(self, nums: List[int]) -> bool: 
        """
        General idea: calculate all possible sums using set and if one of them is equal to half -> return True
        """
        if sum(nums) % 2 == 0:
            target = sum(nums) // 2 
            cur = {0}
            for i in nums:
                cur = cur.union({i + x for x in cur})
                if target in cur:
                    return True
        return False