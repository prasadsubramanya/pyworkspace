import cProfile

def my_func():
    total = 0
    for i in range(1000):
        total += i
    return total

# Profile the function
cProfile.run('my_func()')