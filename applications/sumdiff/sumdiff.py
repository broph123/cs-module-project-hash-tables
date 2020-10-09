"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here


sums = {}
diffs = {}

for num1 in q:
    for num2 in q:
        current_sum = f(num1)+f(num2)
        current_diff = f(num1)-f(num2)

        sums[current_sum] = (num1, num2)
        diffs[current_diff] = (num1, num2)

print(sums)
print(diffs)

# Scan through the keys of SUMS
# for each key, see if you can find a matching key in the DIFFs dict
# if we find a mathcing key, the value in SUMS is (a,b) and values in diffs is (cd)
