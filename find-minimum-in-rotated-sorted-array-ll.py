def findMin(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < nums[r]:
            r = mid
        elif nums[mid] > nums[r]:
            l = mid + 1
        elif nums[mid] == nums[r]:    
            r -= 1
    return nums[l]

nums = [3, 4, 5, 1, 2]
print(findMin(nums))
