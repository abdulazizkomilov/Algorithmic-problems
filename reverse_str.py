def reverseString(s: list) -> list:
    for i in range(len(s)//2):
        s[i], s[(len(s)-i)-1] = s[(len(s)-i)-1], s[i]
    return s
#     0,  1,  2,  3,  4
s = ["h","e","l","l","o"]

# abdulaziz
a = ['z', 'i', 'z', 'a', 'l', 'u', 'd', 'b', 'a']

# print(reverseString(s))
reverseString(s)
reverseString(a)