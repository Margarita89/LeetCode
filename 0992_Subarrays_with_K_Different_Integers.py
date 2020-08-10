from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        """
        General idea: sliding window, use a method to calculate at most K distinct intergers 2 times for K and (K-1). Their difference will be the answer. Use 2 pointers for the left and right borders of the window and a hashmap to control the number of occurences of each letter
        1. Method subarraysWithAtMostKDistinct:
            1. Initilize a lookup defaultdict to store the number of times each letter was encountered in current window [l, r]
            2. Initialize l, r - 2 pointers for the window
            3. Initialize counter and res (to store results)
            4. Traverse s with while loop for r pointer
                1. Update lookup for the letter s[r]
                2. Update counter if the letter s[r] is first time in lookup - so we know how many different letters we have
                3. Increase r
                4. With while loop move left border of the window to be sure that counter doesn't exceed K
                    1. Decrease value of s[l] in lookup
                    2. Decrease counter if there are no more s[l] in lookup
                    3. Increase l
                5. Update res by adding the difference (r-l) - it's the number of subarrays with at most K different integers 
            5. Return res
        2. Substract results from the method for K and (K-1) and return it as an answer as it iwll be exactly K different integers
        """
        
        return self.subarraysWithAtMostKDistinct(A, K) - self.subarraysWithAtMostKDistinct(A, K-1)
    
    def subarraysWithAtMostKDistinct(self, s, k):
        lookup = defaultdict(int)
        l, r, counter, res = 0, 0, 0, 0
        while r < len(s):
            lookup[s[r]] += 1
            if lookup[s[r]] == 1:
                counter += 1
            r += 1   
            while l < r and counter > k:
                lookup[s[l]] -= 1
                if lookup[s[l]] == 0:
                    counter -= 1
                l += 1
            res += r - l 
        return res
            
        