def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


def remove_at(i, s):
    return s[:i] + s[i+1:]


def reverse_string():
    _input = input("Enter the string:- ")
    length = len(_input)
    if length > 2:
        _input = remove_at(length-1, _input)
        _input = remove_at(length-3, _input)
    else:
        print("The string should be more than 2 characters")
        return

    output = _input
    print("The Normal string after deleting is :- ",output)
    output = reverse(output)
    print("The reversed string is :- ", output)


reverse_string()
