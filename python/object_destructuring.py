options = {
    "a":1,
    "b": 2,
    "c": 3,
    "d": "foo"
}

def sum(a, b, c):
    return a + b + c


def sum_with_destructuring(a, b, c, **args):
    return a + b + c

res1 = sum_with_destructuring(**options)
print(f"res1 is: {res1}")

res2 = sum(**options) # this won't work
print(f"res2 is: {res2}")


