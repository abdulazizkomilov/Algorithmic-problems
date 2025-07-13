"""
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


idea:
    sadbutsad
    sad          # return l if haystack l and r value equels to needle
     sad
      sad
       sad
        sad
         sad
          sad

"""

haystack, needle = "sadbutsad", "sad"
haystack_1, needle_1 = "leetcode", "leeto"
haystack_2, needle_2 = "a", "a"

def func(haystack, needle):
  l, r = 0, len(needle)

  for i in range(len(haystack)):
    if haystack[l:r] == needle:
      return l
    l += 1
    r += 1

  return -1


def strStr(haystack, needle):
  l, r = 0, len(needle)

  while r <= len(haystack):
    if haystack[l:r] == needle:
      return l
    l += 1
    r += 1

  return -1

print(func(haystack, needle))
print(func(haystack_1, needle_1))
print(func(haystack_2, needle_2))

print(strStr(haystack, needle))
print(strStr(haystack_1, needle_1))
print(strStr(haystack_2, needle_2))
