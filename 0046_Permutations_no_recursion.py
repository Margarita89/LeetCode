from collections import deque
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        General idea: use bfs approach and deque to store current permutations
        1. Initialize empty deque with [] 
        2. Iterate through nums
            1. Store current len of deque - how many permutations so far
            2. Iterate through these permutations 
                1. Popleft old_permutation
                2. Iterate through all positions in this permutation available for insert
                    1. Create new_permutation by inserting num into old_permutation
                    2. Append new_permutation to permutations 
            3. Return permutations as at the end it contains all required permutations
        """
        permutations = deque()
        permutations.append([])
        for num in nums:
            n = len(permutations)
            for _ in range(n):
                old_permutation = permutations.popleft()
                for j in range(len(old_permutation) + 1):
                    new_permutation = old_permutation[:j] + [num] + old_permutation[j:]
                    permutations.append(new_permutation)
        return permutations
        
        
        
        
        