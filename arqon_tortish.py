def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    return 0

def leftRightDifference(nums: list) -> list:
    l, r = 0, sum(nums)
    result = []
    for num in nums:
        r -= num
        result.append(sign(r - l))
        l += num
    return result