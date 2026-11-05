class Solution:
    def isValid(self, s: str) -> bool:
        valid = {"}" : "{", "]" : "[", ")" : "("}
        stack = []
        for char in s:
            if char in valid:
                if not stack or stack.pop() != valid[char]:
                    return False
            else:
                stack.append(char)
        return not stack
            