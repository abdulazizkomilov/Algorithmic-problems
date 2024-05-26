'''
Eng ko'p suvli hovuz
Sizga orasi 1 metr qilib joylashtirilgan devor balandliklari berilgan. Eng ko'p suv sig'dira oladigan ikkita devor qancha suv sig'dira oladi?

Misol 1:


Kiritma: [1,8,6,2,5,4,8,3,7]
Natija: 49
Tushuntirish: 7 * 7 = 49

Misol 2:
Kiritma: [1,1]
Natija: 1
'''

def maxArea(nums: list) -> int:
    i, j = 0, len(nums) - 1
    max_area = 0
    while i < j:
        area = (j - i) * min(nums[i], nums[j])
        max_area = max(max_area, area)
        if nums[i] < nums[j]:
            i += 1
        else:
            j -= 1
        
    return max_area

print(maxArea([1,8,6,2,5,4,8,3,7]))