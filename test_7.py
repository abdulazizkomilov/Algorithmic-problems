# DESCRIPTION:
# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. 
# You don't have to worry with strings with less than two characters.

# Examples
# "apple" --> 'ppl'
# "conversation"  --> 'onversatio'
# "lizania" --> 'izani'
# "ab" --> ''

# --------------- Answer ---------------

def remove_char(s): 
    return s[1 : -1]