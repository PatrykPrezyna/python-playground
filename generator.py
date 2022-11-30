def gen246():
    print("test1")
    yield (2)
    yield (3)
    print("test2")
    yield (4)


g = gen246()

for i in g:
    print(i)
    print("--")
