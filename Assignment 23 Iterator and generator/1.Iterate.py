l1 = [1,2,3,4,9,8,6]
it = iter(l1)
while True:
    try:
        print(next(it),end=' ')
    except StopIteration:
        break