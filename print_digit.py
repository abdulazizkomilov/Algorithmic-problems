def print_digit(num: int) -> None:
    if num == 0:
        return 0
    while num != 0:
        digit = num % 10
        print(digit)
        num //= 10
