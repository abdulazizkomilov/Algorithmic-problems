def revese_digits(num: int) -> int:
    result = 0
    while num != 0:
        result *= 10
        digit = num % 10
        result += digit
        num //= 10

    return result
