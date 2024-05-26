"""
Kiritish: nums = [1,2,3,4,5,6,7], k = 3
Natija: [5,6,7,1,2,3,4]
Tushuntirish:
1-qadam: [7,1,2,3,4,5,6]
2-qadam: [6,7,1,2,3,4,5]
3-qadam: [5,6,7,1,2,3,4]


Kiritish: nums = [-1,-100,3,99], k = 2
Natija: [3,99,-1,-100]
Tushuntirish: 
1-qadam: [99,-1,-100,3]
2-qadam: [3,99,-1,-100]
"""

def reverse(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
        


def rotate(nums: list, k: int) -> list:
    reverse(nums, 0, len(nums)-1)
    reverse(nums, k, len(nums)-1)
    reverse(nums, 0, k-1)
    
    return nums


nums = [1,2,3,4,5,6,7]
k = 3

print(rotate(nums, k))