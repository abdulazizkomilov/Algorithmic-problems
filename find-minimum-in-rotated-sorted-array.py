def findMin(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    
    return nums[l]

nums = [1,2,3,4,5]
print(findMin(nums))
