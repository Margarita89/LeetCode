class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        General idea: use recursion to find all sums
        1. Sort candidates
        2. Recursion with empty stack:
            1. Base case: target is 0 -> append previous sum to res
            2. Iterate through all items in candidates
                1. If an item is larger than target - break (as candidates are sorted)
                2. If the item is smaller than the last in stack -> continue as is has been checked
                3. Else: start recursion with this item (reduce target and append this item to stack)
        """
        res = []
        candidates.sort()
        
        def combination(target, stack):
            if target == 0:
                res.append(stack)
                return 
            
            for item in candidates:
                if item > target: break
                # skip smaller items that have been already checked
                if stack and item < stack[-1]: continue 
                else:
                    combination(target - item, stack + [item])

        combination(target, [])
        return res
        