"""
rotate image logic

          1             1              1             1
matrix[0][0], matrix[0][0] = matrix[0][0], matrix[0][0]
          2             4              4             2
matrix[0][1], matrix[1][0] = matrix[1][0], matrix[0][1]
          3             7              7             3
matrix[0][2], matrix[2][0] = matrix[2][0], matrix[0][2]

"""


# Input:              Output
#   matrix = [        [
#       [1,2,3],        [7,4,1],
#       [4,5,6],        [8,5,2],
#       [7,8,9]         [9,6,3]
#   ]                 ]


# | Metric    | Value |
# | --------- | ----- |
# | **Time**  | O(N²) |
# | **Space** | O(1)  |



# in-place


matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix_2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix_3 = [
    [1,  2,  3,  4,  5,  6,  7],
    [8,  9, 10, 11, 12, 13, 14],
    [15,16, 17, 18, 19, 20, 21],
    [22,23, 24, 25, 26, 27, 28],
    [29,30, 31, 32, 33, 34, 35],
    [36,37, 38, 39, 40, 41, 42],
    [43,44, 45, 46, 47, 48, 49]
]
matrixes = [matrix_1, matrix_2, matrix_3]

def rotate_img(matrix):
  for idx, arr in enumerate(matrix):
    for i in range(idx):
      matrix[idx][i], matrix[i][idx] = matrix[i][idx], matrix[idx][i]

def reverse_arr(matrix):
  for arr in matrix:
    l, r = 0, len(arr) - 1
    while l < r:
      arr[l], arr[r] = arr[r], arr[l]
      l += 1
      r -= 1

for matrix in matrixes:
  rotate_img(matrix)
  reverse_arr(matrix)
  print(matrix)
