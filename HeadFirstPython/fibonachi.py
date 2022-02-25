import time


def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def fibonacci_new(num):
    global cache
    if num in cache:
        return cache[num]
    if num == 0:
        result = 0
    elif num == 1:
        result = 1
    else:
        result = fibonacci_new(num - 1) + fibonacci_new(num - 2)
    cache[num] = result
    return result


cache = {}
start = time.time()
res = fibonacci(35)
end = time.time()
duration = end - start
print(res, duration)
start = time.time()
res = fibonacci_new(35)
end = time.time()
duration = end - start
print(res, duration)
