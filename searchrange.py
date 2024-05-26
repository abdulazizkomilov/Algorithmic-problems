# def searchRange(nums, target):
#         arr = []
#         for i, num in enumerate(nums):
#             if num == target:
#                 arr.append(i)
#         if arr:    
#             if len(arr) > 1:   
#                 return [arr[0], arr[-1]]
#             else:
#                 return [arr[0], arr[-1]]
#         return [-1, -1]


def searchRange(nums, target):
    first, last = -1, -1
    for i in range(len(nums)-1):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first, last]
                
    
nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target))


nums = [3,3,3]
target = 3
print(searchRange(nums, target))
