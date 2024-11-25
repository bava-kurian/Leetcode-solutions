class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in match.values():
                stack.append(char)
            elif char in match:
                if not stack or stack[-1] != match[char]:
                    return False
                stack.pop()
            else:
                return False
        return not stack
