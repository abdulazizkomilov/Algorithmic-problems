def longestCommonPrefix(words: list) -> str:
    prefix = 0
    short = min(words, key=len)
    n = len(short)
    
    for i in range(n):
        for word in words:
            if short[i] != word[i]:
                return word[:prefix]
            
        prefix = i+1
    
    return short


words = ["flower", "flow", "flight"]

longestCommonPrefix(words)