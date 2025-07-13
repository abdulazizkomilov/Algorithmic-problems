from typing import List


def removeElement(nums: List[int], val: int) -> int:
    i = 0
    
    for item in nums:
        if item != val:
            nums[i] = item
            i += 1
    
    print(nums)
    return i



# nums = [3,2,2,3]
# val = 3

nums = [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(nums, val))


#  Time	 O(n)
#  Space O(1)
