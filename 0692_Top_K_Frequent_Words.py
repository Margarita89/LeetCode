from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        1. use Counter to create a dictionary of words and their frequencies
        2. move all key-value pairs from dictionary to a list
        3. sort the list by values in descending order (use -x[i] for it)
        4. return first k words
        """
        dict_words = Counter(words)
        ans = []
        for key, value in dict_words.items():
            ans.append((key, value))
        
        ans.sort(key= lambda x: (-x[1], x[0]))
        return [x[0] for x in ans[:k]]