# DESCRIPTION:
# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# Example
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

# --------------- Answer ---------------
def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit():
            return True
    return False
