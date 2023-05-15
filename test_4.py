# DESCRIPTION:
# This kata is about multiplying a given number by eight 
# if it is an even number and by nine otherwise.

# --------------- Answer ---------------

def simple_multiplication(n) :
    return n * 8 if n % 2 == 0 else n * 9
