"""
Berilgan ro'yxat ichidan targit sonni toping.
Misol uchun: 
    arr = [1,2,3,4,5,6,7,8,9]
    targit = 6

    binary_search(arr, targit) --> 6
"""

def binary_search(arr: list,  targit: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        print("low: ", low)
        print("high: ", high)
        mid = (low + high) // 2
        print("mid: ", mid)
        guess = arr[mid]
        print("guess: ", guess)

        if guess == targit:
            return mid
        elif guess > targit:
            high = mid - 1
        else:
            low = mid + 1

    return None

arr = list(range(0, 10))
arr2 = list(range(0, 1000))
arr3 = list(range(0, 10000))

print(binary_search(arr, 6))
print(binary_search(arr2, 745))
print(binary_search(arr3, 6876))

