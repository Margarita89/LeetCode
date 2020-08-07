class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        1. Sort products
        2. Iterate through searchWord and increase prefix each time (might be just a slice)
        3. Find the index where to insert prefix in products using bisect_left
        4. Get 3 first words from index if they start with prefix
        """
        products.sort()
        prefix = ''
        ans = []
        
        for ch in searchWord:
            prefix += ch
            i = bisect.bisect_left(products, prefix)
            ans.append([word for word in products[i:i+3] if word.startswith(prefix)])
        return ans