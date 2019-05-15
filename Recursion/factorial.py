def factorial(n):
    """
    Calculate n!

    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """

    # TODO: Write your recursive factorial function here

    if n == 0:
        return 1
    return n * factorial(n-1)


print(factorial(5))
