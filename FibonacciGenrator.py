from re import A


# fibonacci using generator
def fib():
    A, B = 0, 1
    while True:
        yield A
        A, B = B, A+B


for f in fib():
    if f > 50:
        break
    print(f)

    # generators are better than class based iterators as itr() or next() methods are not required
    #stop iteration exception is not required.