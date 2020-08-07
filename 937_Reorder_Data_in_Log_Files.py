class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        General idea: use 2 stacks. 1 for digits and 1 for words
        """
        stack1, stack2 = [], []
        for log in logs:
            words = log.split(' ')
            if words[1].isdigit():
                stack1.append(log)
            else:
                stack2.append(log)
                
        # sort stack2, words and only then identifiers
        stack2.sort(key =lambda x: [x.split()[1:], x.split()[0]])
        return stack2 + stack1
        