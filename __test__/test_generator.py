
def sqaures(n=10):
    for i in range(n):
        yield(i, i**2)


for x in sqaures(20):
    print(x)
