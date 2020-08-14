class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        """
        General idea: there is a cycle. Append every day to the list, when the cycle detected - stop and return (N-1) % cycle
        1. Initialize count (responsible for cycle size) 
        2. While cycle not found:
            1. Create a list called temp to store next day row
            2. Check if it's already in ans, if yes -> break
            3. Else: append the day to ans and update count for cycles. Don't forget to make temp a new cells
        3. Return resulting day by index from ans
        Comment: it might be that N < cycle, it will work also, maybe it's worth adding a checker for that. But since cycle is int - so it's still O(1).
        """                
        count = 0
        ans = []
        while True:
            temp = [0]
            for j in range(1, len(cells) - 1):
                if cells[j-1] == cells[j+1]:
                    temp.append(1)
                else:
                    temp.append(0)
            temp.append(0)

            if ans and ans[0] == temp:
                break
            else:
                ans.append(temp)
                count += 1
                cells = tuple(temp)
        
        return ans[(N-1) % count]
