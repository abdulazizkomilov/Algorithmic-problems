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


def maxDepth(s: str) -> int:
    brackets = {')', '(', ']', '[', '}', '{'}
    pairs = {')': '(', ']': '[', '}': '{'}
    count = 0
    stack = []
    
    for i in s:
        if i in brackets:
            stack.append(i)
            if stack[-1] == i and i in pairs:
                stack.pop()
                stack.pop()
                
            if count < len(stack):
                count = len(stack)
        
    return count

s = "(1+(2*3)+((8)/4))+1"
print(maxDepth(s))

s = "(1)+((2))+(((3)))"
print(maxDepth(s))

s = "()(())(((())()))"
print(maxDepth(s))
