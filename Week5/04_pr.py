def test():
    i = 0
    for _ in range(10):
        i += 1
        return i
def test2():
    j = 0
    for _ in range(10):
        j += 1
    return j
print("test() is ", test())
print("test2() is ", test2())