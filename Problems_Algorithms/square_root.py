def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        raise Exception("Number cannot be less than 0")
    if number == 0:
        return 0
    return sqrt_helper(number, 0, number)


def sqrt_helper(number, left, right):

    middle = left + (right-left)/2
    difference = number/middle - int(middle)
    if difference >= 0 and difference < 1:
        return int(middle)
    if number//middle < middle:
        return sqrt_helper(number, 0, middle)
    else:
        return sqrt_helper(number, middle, right)


# Test Case 1 - Normal integer
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

# Test Case 2 - Negative integer
try:
    temp = sqrt(-100)
except Exception:
    print("the number cannot be less than 0")

# Test Case 3 - Very Large Integer
print("Pass" if (3162 == sqrt(10000000)) else "Fail")
print("Pass" if (3513641828 == sqrt(12345678901234567890)) else "Fail")
