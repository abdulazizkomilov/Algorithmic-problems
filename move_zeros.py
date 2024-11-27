def moveZeroes(nums: list) -> list:
	count = 0
	for i, n in enumerate(nums):
		if n == 0:
			count += 1
			continue
		nums[i], nums[i-count] = nums[i-count], nums[i]
	return nums

nums = [0,1,0,3,12]

print(moveZeroes(nums))
