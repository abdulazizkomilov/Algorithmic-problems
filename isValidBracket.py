"""
Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([])"
Output: true


(
 [
  ]
   )

[
  '(', '[',
]

"""


def isValid(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for i in s:
        if i in pairs.values():
            stack.append(i)
        elif i in pairs:
            if not stack or stack[-1] != pairs[i]:
                return False
            stack.pop()
    
    return not stack

print(isValid(")()[]([()])(")) # False
print(isValid("()[]{}"))       # True
print(isValid("(]"))           # False
print(isValid("([])"))         # True
print(isValid("()[]([()])("))  # False
print(isValid("()[]{}"))       # True
print(isValid("(]"))           # False
print(isValid("([])"))         # True
print(isValid("([)]"))         # False


