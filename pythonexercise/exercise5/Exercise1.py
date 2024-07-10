n = int(input("Please enter a number."))
dict = {}
dict = {i: list(i * "*") for i in range(1,n+1)}
print(dict)