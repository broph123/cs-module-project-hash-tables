# Your code here
import math
import random

num_table = {}


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    v = math.pow(x, y)

    if v not in num_table:
        num_table[v] = math.factorial(v)
        value = num_table[v]
        value //= (x + y)
        value %= 982451653
        return value

    else:
        stored = num_table[v]
        stored //= (x+y)
        stored %= 982451653
        return stored


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
