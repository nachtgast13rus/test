import time


def fibonachi(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonachi(num - 1) + fibonachi(num - 2)


for i in range(1, 50, 5):
    start = time.time()
    res = fibonachi(i)
    end = time.time()
    duration = end - start
    print(i, res, duration)
