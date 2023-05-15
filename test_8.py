# DESCRIPTION:
# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

# Use conditionals to return the proper message:

# case ----------------------- return
# ------------------------------------------
# name equals owner	--------- 'Hello boss'
# otherwise	----------------- 'Hello guest'

# --------------- Answer ---------------

def greet(name, owner): return 'Hello boss' if name == owner else 'Hello guest'