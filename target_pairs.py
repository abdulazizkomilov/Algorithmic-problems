# Input: nums = [1,2,3,6,7,8,11,15], target = 9

# Output: [(0, 5), (1, 4), (2, 3)]

# Explanation: Because
    # nums[0] + nums[5] == 9, 
    # nums[1] + nums[4] == 9,
    # nums[2] + nums[3] == 9,
    
    # we return [(0, 5), (1, 4), (2, 3)]


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def find_target_pairs(nums, target):
    pairs = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print(f"{nums[i]} + {nums[j]}: {target}")
                pairs += 1
    return pairs


print(find_target_pairs(nums, target=10))

















