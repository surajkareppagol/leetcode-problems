# Author: Suraj K

from typing import *


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if stack and bracket == ")" and stack[-1] == "(":
                stack.pop()
                continue
            elif stack and bracket == "]" and stack[-1] == "[":
                stack.pop()
                continue
            elif stack and bracket == "}" and stack[-1] == "{":
                stack.pop()
                continue

            stack.append(bracket)

        if not stack:
            return True
        return False


s = Solution()

print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([])"))
