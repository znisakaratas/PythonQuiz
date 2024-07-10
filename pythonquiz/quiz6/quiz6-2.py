import sys
n = int(sys.argv[1])
increase = [i for i in range(1, n)]
decrease = [j for j in range(n,0,-1)]
diamond = increase + decrease
for e in diamond:
    print(((n - e) * " ") + ((2 * e) - 1) * "*")
