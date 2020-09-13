class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        """
        General idea: use sliding window with start from 0 index and end running through all trees
        1. Initialize a dictionary to store different fruits and their counter, start index and max_fruits so far
        2. Iterate with end index through all trees
            1. right_tree - is current tree
            2. if right_tree not yet in fruit_baskets -> add it to the fruit_baskets
            3. else: update its counter in fruit_baskets
            4. Use while loop for the length of the fruit_baskets (> 2) to move start index
                1. left_tree - is tree at index start
                2. Decrease fruit_baskets of left_tree
                3. if counter of fruit_baskets of left_tree becomes 0 -> delete this key-value pair
                4. Increase start index
            5. Update max_fruits (after while loop fruit_baskets has no more than 2 different fruits)
        3. Return max_fruits
        """
        fruit_baskets = {}
        start = 0
        max_fruits = 0
        for end in range(len(tree)):
            right_tree = tree[end]
            if right_tree not in fruit_baskets:
                fruit_baskets[right_tree] = 0
            fruit_baskets[right_tree] += 1
            
            while len(fruit_baskets) > 2:
                left_tree = tree[start]
                fruit_baskets[left_tree] -= 1
                if fruit_baskets[left_tree] == 0:
                    del fruit_baskets[left_tree]
                start += 1
            max_fruits = max(max_fruits, end - start + 1)
        return max_fruits
            