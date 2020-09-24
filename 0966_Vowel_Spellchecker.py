class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        General idea: prepare 1 set of words from wordlist if the words are identical and 2 dictionaries from wordlist for capital and vowels (with first word occurances -> use setdefault). For comparison of words with different vowels use vowel mask. 
        1. mask_vowel method -> return string with inserted '*' insead of vowels
        2. Initialize words_exact as set of wordlist, words_capit and words_vowel empty
        3. Iterate through words in wordlist
            1. Setdefault (create key-value if not there) for words_capit and words_vowel of word_low: word. Maybe not the best as setdefault returns value and here there is no need to return
        4. find method for query:
            1. If query in words_exact -> return query
            2. If query_low in words_capit -> return value (it's first word in initial form)
            3. If query_low with masked vowels in words_vowel -> return value (it's first word in initial form)
            4. Else -> return ''
        5. Return map from find method and a list of queries
        """
        def mask_vowel(word):
            return "".join('*' if c in 'aeiou' else c
                           for c in word)

        words_exact = set(wordlist)
        words_capit = {}
        words_vowel = {}

        for word in wordlist:
            word_low = word.lower()
            words_capit.setdefault(word_low, word)
            words_vowel.setdefault(mask_vowel(word_low), word)

        def find(query):
            if query in words_exact:
                return query

            query_low = query.lower()
            if query_low in words_capit:
                return words_capit[query_low]

            query_low_vow = mask_vowel(query_low)
            if query_low_vow in words_vowel:
                return words_vowel[query_low_vow]
            return ""

        return map(find, queries)