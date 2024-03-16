"""
Berilgan son raqamlarini ekranga chiqaring.
Misol uchun: print_digits(123) 
Natija quyidagicha chiqsin:
3
2
1

M: 76
N:
6
7

"""

def print_digits(num: int) -> None:
    if num == 0:
        print(0)
        return
    
    while num != 0:
        digit = num % 10. # 123 % 10 = 3
        print(digit)
        num //= 10.   # 123 // 10 = 12

print(print_digits(123))
print('\n')
print(print_digits(456))
print(print_digits(0))

