class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        """
        General idea: use dfs (recursively permute)
        1. Convert strings to lists as strings are immutable 
        2. Use recursive swap method with index and current swaps
            1. Base case: index reached the end (last letters are the same as by condition and there were enough swaps). Or the last of the strings are equal - no need to swap longer -> update self.counter and return
            2. Iterate from first index
                1. If letters are different:
                    1. Iterate through B to find equal letter to swap
                        1. If the letter is found and current swaps counter is smaller than self.counter (otherwise we can't minimize - no need to work on this swap) -> swap letters in B, perform swap recursively and swap letters back in B
                    2. Break as we are looking only for the first difference in letters
            3. Return
        3. Perform swap from first index = 0 and current swap sum = 0
        4. Return self.counter
        """
        self.counter = float('inf')
        A = list(A)
        B = list(B)
        
        def swap(first, cur):
            if first == len(A) - 1 or A[first:] == B[first:]:
                self.counter = min(self.counter, cur)
                return
            for i in range(first, len(A)):
                if A[i] != B[i]:
                    for k in range(i + 1, len(A)):
                        if A[i] == B[k] and cur + 1 < self.counter:
                            B[i], B[k] = B[k], B[i]
                            swap(i + 1, cur + 1)
                            B[i], B[k] = B[k], B[i]
                    break
            return 
            
        swap(0, 0)
        return self.counter