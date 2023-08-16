# DESCRIPTION:
# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.


# Example
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

# --------------- Answer ---------------
def high_and_low(numbers):
    numbers = [int(num) for num in numbers.split()]

    high = numbers[0]
    low = numbers[0]

    for _ in numbers:
        if high < _:
            high = _
        if low > _:
            low = _

    return str(high) + " " + str(low)
