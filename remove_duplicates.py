nums = [1,1,2]

# def removeDuplicates(nums: list[int]) -> int:
#     if not nums:
#         return 0

#     unique_num = 1
#     for i in range(1, len(nums)):
#         if nums[i] != nums[i - 1]:
#             nums[unique_num] = nums[i]
#             unique_num += 1
    
#     return unique_num
                
# print(removeDuplicates(nums))


from collections import Counter

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

num_counts = Counter(nums)
print(len(num_counts.keys()))
