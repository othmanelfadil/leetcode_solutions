# O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_closed = {')':'(' , '}':'{' , ']':'['}
        for c in s:
            if c in open_closed:
                if stack and stack[-1] == open_closed[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False 