class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        """
        General idea: use bfs approach and add each character to existing permutations
        1. Initialize a list with empty string
        2. Iterate through characters in S
	        1. Initialize empty list tmp
	        2. Iterate through permutations
		        1. If character is string -> append current permutation with upper and lower character to tmp list
		        2. Else -> just append current permutation to tmp list 
	        3. Make permutations be equal to tmp
        3. Return permutations
        """
        permutations = ['']
        for ch in S:
            tmp = []
            for old_permutation in permutations:
                if ch.isalpha():
                    tmp.append(old_permutation + ch.upper())
                    tmp.append(old_permutation + ch.lower())
                else:
                    tmp.append(old_permutation + ch)
            permutations = tmp
        return permutations