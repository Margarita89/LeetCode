from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        """
        General idea: use Counter to calculate frequencies of each character and then insert them into answer on every second place
        1. Inialize empty temp list
        2. Use Counter for string S to calculate frequencies of each character. Store result into counter_s also applying most_common() method and sorting in descending order 
        3. Iterate through counter_s
            1. If count of character is larger than half (in even case and larger than lens // 2 + 1 in odd case) - > return empty string
            2. Extend temp by adding this character count times
        4. Initialize empty list of ans
        5. Let every even position in ans be first half of tmp and every odd position in ans be second half of tmp
        6. Return joined ans
        Example: 'aab'
        counter_s = {'a': 2, 'b': 1}, temp = ['a', 'a', 'b']
        temp[:2] = ['a', 'a'], temp[2:] = ['b']
        ans[0] = 'a', ans[2] = 'a', ans[1] = 'b'
        """
        lens = len(S)
        temp = []
        counter_s = Counter(S).most_common()
        for x, count in counter_s:
            if count > lens // 2 + lens % 2: # == (lens + 1) // 2
                return ''
            temp.extend(x * count)
        ans = [None] * lens
        ans[::2], ans[1::2] = temp[:lens // 2 + lens % 2], temp[lens // 2 + lens % 2:]
        return ''.join(ans)
        