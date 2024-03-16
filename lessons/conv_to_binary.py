"""
Berilgan son ikkilik sanoq songa o'tkazing.
Misol uchun: 
    convert_to_binary(6) --> "110"
    convert_to_binary(8) --> "1000"
"""

def convert_to_binary(num: int) -> str:
    result = ""

    while num != 0:
        digit = num % 2
        result += str(digit)
        num //= 2

    return result[::-1]

print(convert_to_binary(6))
print(convert_to_binary(8))
print(convert_to_binary(16))
print(convert_to_binary(879))
print(convert_to_binary(32))
