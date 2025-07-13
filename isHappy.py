"""
Example 1:

Input: n = 19
Output: true
Explanation:
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1


Example 2:

Input: n = 2
Output: false

2² = 4
4² = 16
1² + 6² = 37
3² + 7² = 58
5² + 8² = 89
8² + 9² = 145


"""

n_1 = 19
n_2 = 2



class Solution:
    def num_square_sum(self, n: int) -> int:
        r = 0
        while n > 0:
            num = n % 10
            r += num * num
            n = n // 10
        return r

    def isHappy(self, n: int) -> bool:
        result = set()
        
        while True:
            sum_n_square = self.num_square_sum(n)
            
            if sum_n_square == 1:
                return True
            
            if sum_n_square not in result:
                result.add(sum_n_square)
            else:
                return False
            
            n = sum_n_square

s = Solution()
print(s.isHappy(n_1))
print()
print(s.isHappy(n_2))


# | Metric | Complexity |
# | ------ | ---------- |
# | Time   | O(log n)   |
# | Space  | O(1)       |


