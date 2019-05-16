def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):

    result = []
    if num < 10:
        return list(get_characters(num))
    else:
        first_number = int(str(num)[0])
        rest_number = int(str(num)[1:])
        sub_keypad_combo = keypad(rest_number)
        for c in get_characters(first_number):
            result += [c+sub for sub in sub_keypad_combo]
    return result


print(keypad(23))
