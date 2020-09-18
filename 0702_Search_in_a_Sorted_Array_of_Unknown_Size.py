class Solution:
    def search(self, reader, target):
        """
		General idea: first find start and end using reader and mutliplying end by 2 each time and then use binary seach
		1. Initalize end = 1
		2. Use while loop with reader.get while result is less than target to find upper boundary
			1. Muliplu end by 2
		3. start is end // 2
		4. Binary seach to find target and return index if found
		5. Return -1 (in case there is no return from while loop)
        """
        end = 1
        while reader.get(end) < target: 
        	end *= 2
        start = end // 2

        while start <= end:
            mid = (start + end) // 2
            val = reader.get(mid)
            if val == target: 
            	return mid
            if val > target:
                end = mid -1
            else:
                start = mid + 1

        return -1