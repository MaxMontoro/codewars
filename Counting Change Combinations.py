cache = {}
def count_change(n, integers=tuple(range(1,280))):
    integers = tuple(integers)
    if (n, integers) in cache:
        return cache[(n, integers)]
    if n < 0:
        return 0
    elif n == 0:
        return 1
    if n > 0 and len(integers) == 0:
        return 0
    else:    
        largest, rest = integers[0], integers[1:] 
    cache[(n-largest, integers)] = count_change(n-largest, integers)
    cache[(n, rest)] = count_change(n, rest)
    return cache[(n-largest, integers)] + cache[(n, rest)]