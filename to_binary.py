def convert_to_binary(num: int) -> str:
    result = ''
    while num != 0:
        digit = num % 2
        result += str(digit)
        num //= 2

    return result[::-1]
