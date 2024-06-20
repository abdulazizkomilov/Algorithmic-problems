def is_valid(s: str) -> bool:
    balance = 0

    for i in s:
        if i == '(':
            balance += 1
        elif i == ')':
            balance -= 1

        if balance < 0:
            return False

    return balance == 0

s = "((()))"
b = "((())"

is_valid(s)
is_valid(b)