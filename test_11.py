# DESCRIPTION:
# Sentence Smash
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

# Example
# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

# --------------- Answer ---------------

def smash(words):
    a = ''
    if len(words) > 1:
        a += words[0]
        for _ in words[1:]:
            a += ' ' + _
        return str(a)
    elif len(words) <= 0:
        return ''
    else:
        a = ''
        for _ in words:
            a += _
        return a
    
# After I learned .join
def smash(words): return " ".join(words)