"""
Berilgan son raqamlarini teskari son qilib qaytaring.
Misol uchun: 
    reverse_digits(123) --> 321
    reverse_digits(456) --> 654
"""

def reverse_digits(num: int) -> int:
    result = 0

    while num != 0:
        result *= 10  # result = result * 10
        digit = num % 10
        result += digit
        num //= 10
    
    return result


print(reverse_digits(123))
print(reverse_digits(710))
print(reverse_digits(8734))