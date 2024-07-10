n = input("Please enter 10 numbers ")
newlist = n.split(" ")
nlist = list()
for i in newlist:
    nlist.append(int(i))
    nlist.sort()
def recnumbers():
    if len(nlist) == 10:
        summ = 0
        for i in nlist:
            summ += int(i)
            average = summ / 10
        nlist.pop(5)
        return recnumbers() + " " + "Average of list:" + str(average)
    elif len(nlist) == 9:
        nlist.pop(4)
        return "Maximum of numbers:" + str(max(nlist)) + " " + recnumbers()
    else:
        return "Minimum of numbers:" + str(min(nlist))
print(recnumbers())