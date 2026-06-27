class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs)
        ans = ""
        for index, char in enumerate(shortest):
            for string in strs:
                if string[index] != char:
                    return ans
            ans += char
        
        return ans

        





        