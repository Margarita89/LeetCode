class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        General idea: use hash map to store (target - element) and element's index
        - it will allow to check if element is in hash map
        """
        map = {}
        for i, elem in enumerate(nums):
            if elem not in map:
                map[target - elem] = i
            else:
                return [map[elem], i]
        
        
        