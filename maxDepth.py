"""
Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3

Explanation:
Digit 8 is inside of 3 nested parentheses in the string.

Example 2:

Input: s = "(1)+((2))+(((3)))"
Output: 3

Explanation:
Digit 3 is inside of 3 nested parentheses in the string.

Example 3:

Input: s = "()(())((()()))"
Output: 3


count = 0


"""


def maxDepth(self, s: str) -> int:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    max_depth = 0

    for char in s:
        if char in pairs.values():
            stack.append(char)
            max_depth = max(max_depth, len(stack))
        elif char in pairs:
            if stack and stack[-1] == pairs[char]:
                stack.pop()

    return max_depth if not stack else -1

s = "(1+(2*3)+((8)/4))+1"
print(maxDepth(s))

s = "(1)+((2))+(((3)))"
print(maxDepth(s))

s = "()(())(((())()))"
print(maxDepth(s))
