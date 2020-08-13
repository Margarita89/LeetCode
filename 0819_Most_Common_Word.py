class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """
        1. Turn banned into set to decrease time to search in banned
        2. Replace all signes in paragraph with spaces
        3. Use Counter to store a hashmap 'count' with words and their frequencies
        4. Iterate through 'count' and if word not in banned -> update most common word if needed
        """
        banned = set(banned)
        for ch in "!?.,;':":
            paragraph = paragraph.replace(ch, ' ')
        count = collections.Counter(word for word in paragraph.lower().split())
        max_freq, most_common = 0, ''
        for word in count:
            if word not in banned and count[word] > max_freq:
                    max_freq = count[word]
                    most_common = word
        return most_common
                    
                    