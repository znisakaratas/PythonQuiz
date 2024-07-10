import sys
try:
    base = int(sys.argv[1])
    exponent = int(sys.argv[2])
    number = (base ** exponent)
    total = 0
    final_total = 0

    while number > 0:
        firstdigit = number % 10
        number = int(number / 10)
        total += firstdigit
    if len(str(total)) == 1:
        print(total)
    else:
        while len(str(total)) > 0 and total != 0:
            digit = total % 10
            total = int(total / 10)
            final_total += digit
        if len(str(final_total)) == 1:
            print(final_total)
        elif len(str(final_total)) == 2:
            x = final_total % 10
            final_total //= 10
            p = x + final_total
            if len(str(p)) == 1:
                print(p)
            elif len(str(p)) == 2:
                print(p % 10 + p // 10)

except:
    pass
