# def detectCapitalUse(word: str) -> bool:
# 	if word.isupper() or word.islower():
#         return True

#     return word[:1].isupper() and word[1:].islower()

def in_range(s, start, end):
    for i in s:
        if not ord(start) <= ord(i) <= ord(end):
            return False
    return True

def isupper(s):
    return in_range(s, 'A', 'Z')

def islower(s):
    return in_range(s, 'a', 'z')

def detectCapitalUse(word: str) -> bool:
    if isupper(word) or islower(word):
        return True

    return isupper(word[:1]) and islower(word[1:])
