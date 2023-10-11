# Input: x = 123
# Output: 321


class Solution:
    def reverse(self, x: int) -> int:
        max_ = (2 ** 31) -1
        min_ = -2 ** 31
        num = 0
        if x > 0:
            while x > 0:
                num += x % 10
                num *= 10
                x //= 10
            if min_ <= num and x <= max_:
                return num // 10
            else:
                return 0
        else:
            x *= -1
            while x > 0:
                num += x % 10
                num *= 10
                x //= 10
                
            num //= 10
            
            if min_ <= num and x <= max_:
                return num * (-1)
            else:
                return 0

    
a = Solution()

a.reverse(123)










