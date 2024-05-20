'''
Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1
'''


def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))

nums1 = [1,3,5,6]
target1 = 0
print(searchInsert(nums1, target1))

nums2 = [1,2,3,5,6,7,8] 
target2 = 4
print(searchInsert(nums2, target2))

