class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        General idea: use start as starting index of previous range, when there is a gap between numbers, use this start and previous number as range
        1. Base case: empty nums -> return empty list
        2. Initialize empty stack, and start as 0
        3. Iterate through nums
            1. If there is a gap between current and previous num -> append [start -> end] to the stack (previous range). Update start to current
        4. Append last range to stack
        5. Return stack
        """
        def makeRange(start, end):
            if start == end:
                stack.append(str(nums[start]))
            else:
                stack.append(str(nums[start]) + '->' + str(nums[end]))
            
        if not nums:
            return []
        stack = []
        start = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                makeRange(start, i-1)
                start = i
        makeRange(start, len(nums) - 1)
        return stack