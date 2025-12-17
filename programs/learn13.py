# from functools import lru_cache
# @lru_cache(maxsize=128)
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(10))

cache = {}
def expensive_function(x):
    if x in cache:
        return cache[x]             # return cached value
    
    print("Computing...")
    result = x * x                  # expensive logic
    cache[x] = result               # store result
    return result

print(expensive_function(10))
print(expensive_function(10))