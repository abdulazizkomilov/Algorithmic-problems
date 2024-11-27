def reverse(nums, first, last):
	while first < last:
		nums[first], nums[last] = nums[last], nums[first]
		first += 1
		last -= 1


def rotate(nums: list, k: int) -> list:
    if len(nums) < k:
        return nums[::-1]
    reverse(nums, 0, len(nums)-1)
    reverse(nums, k, len(nums)-1)
    reverse(nums, 0, k-1)
    return nums


nums = [1,2,3,4,5,6,7]
k = 3


print(rotate(nums, k))
print(rotate(nums, 8))
