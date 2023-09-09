# def twoSum(nums: list[int], target: int) -> list[int]:
#     first_map = {}
#     print(first_map)
#     for i, n in enumerate(nums):
#         print(i, n)
#         diff = target - n
#         print('diff', '=', target, '-', n, diff)
#         if diff in first_map:
#             print('if ishladi', first_map[diff], i)
#             return [first_map[diff], i]
#         print('> ', first_map)
#         first_map[n] = i
#         print('< ', first_map)
#         print('if not', first_map[n], '=', i)
#     return


# # print(twoSum(nums=[2, 7, 11, 15], target=9))
# print(twoSum(nums=[3, 2, 4], target=6))
# # print(twoSum(nums=[3, 2, 4, 12, 8], target=10))


def twoSum(nums: list[int], target: int) -> list[int]:
    f = {}
    for i, n in enumerate(nums):
        kichik = target - n
        if kichik in f:
            return [f[kichik], i]
        f[n] = i
    return


print(twoSum(nums=[3, 2, 4], target=6))
