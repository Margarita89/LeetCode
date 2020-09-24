class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        General idea: just compare neighboring words
        1. Create dictionary 'dic' with pairs letter and it's order (index) to make comparisons easier
        2. Iterate through pairs of neighboring words using zip
            1. If first word 'a' is longer than second word 'b' and the beginning is the same -> return False (ex.: 'apple' > 'app' is False)
            2. Iterate through letters in both words pairwise
                1. If letter of word 'a' is lexicographicaly smaller than in 'b' -> break
                2. If letter of word 'a' is lexicographicaly larger than in 'b' -> return False
        3. Return True (no False was detected)
        """
        dic = {c: i for i, c in enumerate(order)}
        for a, b in zip(words, words[1:]):
            if len(a) > len(b) and a[:len(b)] == b:     # apple > app
                return False 
            for ch1, ch2 in zip(a, b):
                if dic[ch1] < dic[ch2]:
                    break
                if dic[ch1] > dic[ch2]:
                    return False
        return True