from collections import Counter
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        """
        i = 0 -> A[1] = 2 * A[0]
        i = 1 -> A[3] = 2 * A[2]
        1. Use Counter to count elements in A
        2. Sort A by absolute values. If A = [4, -2, 2, -4], sorted A = [-2, 2, 4, -4]
        3. Iterate through elements in A
        4. Subtract 1 from count[x] and count[2*x]
        5. If count[x] is 0, just continue
        6. If count[2*x] is 0 -> return False as it means count[x] != 0
        """
        count = Counter(A)
        A.sort(key = abs)

        for x in A:
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            
            count[x] -= 1
            count[2*x] -= 1
        
        return True