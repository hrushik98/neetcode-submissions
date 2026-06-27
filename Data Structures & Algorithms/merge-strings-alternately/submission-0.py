class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) < len(word2):
            target = word1
            non_target = word2
        else:
            target = word2
            non_target = word1
        ans = []
        for index, char in enumerate(target):
            ans.append(word1[index])
            ans.append(word2[index])
        
        for i in range(index+1, len(non_target)):
            ans.append(non_target[i])
        
        return "".join(ans)
        