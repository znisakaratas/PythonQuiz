import sys
try:
    n = int(sys.argv[1])
    mylist = []
    for i in range(1,n+1):
        mylist.append(i)
    index = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            mylist.remove(i)
    i = 1
    while len(mylist) >= index:
        index = mylist[i]
        a = index - 1
        del mylist[a::index]
        i += 1
    print(mylist)
except:
    pass