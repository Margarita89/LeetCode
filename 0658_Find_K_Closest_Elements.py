class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        General idea: use heap and add tuples: absolute differences of elements from arr and x (negative as it's a min-heap), also add elements (again negatives to be sure that smaller elements will be kept in case of tie).
        1. Initialize empty heap
        2. Iterate through elements of arr
            1. Push a tuple: absolute difference (with minus) and minus element
            2. If index exceeds k -> alsp pop from heap
        3. Create a list of elements from heap
        4. Sort list and return
        """
        heap = []
        for i, y in enumerate(arr):
            heappush(heap, (-abs(x-y), -y))
            if i >= k:
                heappop(heap)
        res = [-y for z, y in heap]
        res.sort()
        return res