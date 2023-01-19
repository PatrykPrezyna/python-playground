# variable argument list, named and positional parameters


def MyFunction(arg1, *args):
    """ "
    Parameters:
    some documentations
    """
    sum = arg1
    for arg in args:
        sum = sum + arg
    return sum


print(MyFunction.__doc__)
print(MyFunction(1, 2, 3, 4))
list1 = [1, 2, 3, 4]
print(MyFunction(*list1))


# anonymous functions - lambda (like callback in js)
# lambda (parameters): expresion
ctemp = [1, 34, 0, 40]
print(list(map(lambda t: (t - 32) * 5 / 9, ctemp)))

# usinf keyword-only arguments
def critical(x, *, alert=False):
    print("alert", alert)


critical(1, alert=True)
