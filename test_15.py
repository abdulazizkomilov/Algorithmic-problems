# DESCRIPTION:
#

# Example
# -------------------  _     -------- -------
# [1,2,3,4,5,6,7,8,9], 5  => [1,2,3,4,6,7,8,9]

# --------------- Answer ---------------
nums = list(range(1, 10))
print(nums)


def pass_num(nums, index):
    return nums[:index-1] + nums[index:]


print(pass_num(nums, 2))
