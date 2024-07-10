mylist = [1000, 298, 3579, 100, 200, -45, 900]
mylist.sort()
print("My sorted list:",mylist )
n = int(input("Please enter a number."))
print(mylist[-1*n:])
x = int(input("Please enter a number."))
nlist = [mylist[x]]
print(nlist)
y = int(input("Please enter a number."))
newlist = mylist[y-1]
print(newlist)