def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    
    original = x
    reversed_x = 0
    
    while x > 0:
        reversed_x = reversed_x * 10 + x % 10
        x = x // 10

    return original == reversed_x

x = 321
print(isPalindrome(x))
