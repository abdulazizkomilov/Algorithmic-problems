# 24

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        print('guess: ',guess)
        print('mid: ',mid)
        print('low : ',low)
        print('high: ',high)
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


arr = list(range(1726))
print(binary_search(arr, 24))
