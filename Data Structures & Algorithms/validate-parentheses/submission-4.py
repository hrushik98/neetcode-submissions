class Solution:
    def isValid(self, s: str) -> bool:
        # closeToOpen = {
        #     ")": '(',
        #     "]": "[",
        #     "}": "{"
        # }
        # stack = []

        # for char in s:
        #     if char in closeToOpen and not stack:
        #         return False
        #     elif char in closeToOpen and stack[-1] == closeToOpen[char]:
        #         stack.pop()
        #     else:
        #         stack.append(char)
        
        # return True if not stack else False
        cto = {
            "]" : "[",
            "}": "{",
            ")":"("
        }

        stack = []

        for char in s:
            if char in cto and not stack:
                return False 
            elif char in cto and stack[-1] ==cto[char]:
                stack.pop()
            else:
                stack.append(char)
        
        return True if not stack else False

