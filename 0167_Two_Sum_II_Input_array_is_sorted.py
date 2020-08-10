class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        General idea: use 2 pointers - left and right in list of numbers
        1. Initialize 2 pointers 
        2. Traverse a list of numbers with while loop
            - if sum of left and right values equal target -> return answer
            - elif sum of left and right values is larger then target -> move right pointer to left
            - else: move left pointer to right
        """
        l, r = 0, len(numbers)-1
        while l < len(numbers) and r >= 0:
            
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
                