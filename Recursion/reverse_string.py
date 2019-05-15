def reverse_string(input):
    """
    Return reversed input string

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """
    if input == "":
        return ""
    return input[-1] + reverse_string(input[:len(input)-1])


print(reverse_string('abc'))
