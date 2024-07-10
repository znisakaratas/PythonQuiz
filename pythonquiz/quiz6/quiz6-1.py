import sys
n = int(sys.argv[1])


def increase(x):
    def decrease(y):
        if y == 0:
            return ""
        elif y <= n:
            return ((n - y) * " ") + ((2 * y) - 1) * "*" + "\n" + decrease(y - 1)
    if x == n:
        return increase(x + 1) + decrease(x)
    elif x < n:
        if x + 1 == n:
            return ((n - x) * " ") + ((2 * x) - 1) * "*" + "\n"
        else:
            return ((n - x) * " ") + ((2*x) - 1) * "*" + "\n" + increase(x + 1)
    elif x == n + 1:
        return increase(1)


print(increase(n))
