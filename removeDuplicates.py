from typing import List


def removeDuplicates(nums: List[int]) -> int:
    l, r = 0, 1
    
    while r < len(nums):
    
        if nums[l] == nums[r]:
            nums.pop(r)
        else:
            l += 1
            r += 1

    return nums


nums = [0,0,1,1,1,2,2,3,3,4]

# print(removeDuplicates(nums))

# space O (1)
# time  O (n^2)


def removeDuplicates2(nums: List[int]) -> int:
    if not nums:
        return 0
    
    l = 0
    for r in range(1, len(nums)):
        
        if nums[l] != nums[r]:
            l += 1
            print("nums =", nums)
            nums[l] = nums[r]
            print("nums", nums)
    
    print(nums)
    return l + 1

print(removeDuplicates2(nums))

# space O (1)
# time  O (n)


