def isValid(s: str) -> bool:
    brackets = {
        ")": "(", 
        "}": "{", 
        "]": "["
        }
    lst = []
    
    for bracket in s:
        if bracket in "({[":
            lst.append(bracket)
        elif bracket in ")}]":
            if not lst or lst[-1] != brackets[bracket]:
                return False
            lst.pop()
            
    return not lst

s = "()"
s2 = "()[]{}"
s3 = "(]"
print(isValid(s))
