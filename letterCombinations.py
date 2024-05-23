def letterCombinations(digits):
    if not digits:
        return []
    
    num_to_letters = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }
    
    result = []
    
    def backtrack(index, path):
        print(index, path)
        print(result)
        if index == len(digits):
            result.append("".join(path))
            print(result)
            return
        
        current_digit = digits[index]
        for letter in num_to_letters[current_digit]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    
    backtrack(0, [])
    
    return result

digits = "23"
print(letterCombinations(digits))


