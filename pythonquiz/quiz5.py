import sys

def round_numbers(x):
    if "." in x:
        decimal = x.find('.')
        if int(x[decimal+1]) >= 5:
            return int(float(x)) + 1
        else:
            return int(float(x))
    else:
        return int(float(x))

try:
    f = sys.argv[1]
    f2 = sys.argv[2]
    operands = open(f, "r")
    operands_t = open(f, "a")
    operands_t.write("\n")
except IOError:
    print("IOError: cannot open {}".format(f))
except IndexError:
    print("IndexError: number of files less than expected.")
except Exception:
    print("kaBOOM: run for your life.")
try:
    comparison = open(f2, "r")
    com_data = open(f2, "a")
    com_data.write("\n")
except IOError:
    print("IOError: cannot open {}".format(f2))
except NameError:
    pass
except Exception:
    print("kaBOOM: run for your life.")
else:
    result = ""
    while True:
        operand_line = operands.readline()
        comparison_line = comparison.readline()
        if len(operand_line) > 1:
            print("------------")
            lines = operand_line[0:-1].strip()
            numberlist = lines.split(" ")
            try:
                from_num = round_numbers(numberlist[2])
                to_num = round_numbers(numberlist[3])
                div = round_numbers(numberlist[0])
                nondiv = round_numbers(numberlist[1])
                numbers = ""
                for j in range(from_num, to_num + 1):
                    if j % div == 0 and j % nondiv != 0:
                        numbers += str(j) + " "
                        numbers.strip()
                result_line = "My results: {}".format(numbers)
                assert (numbers[0:-1] == comparison_line[0:-1])
                print("My results:               ", numbers[0:-1])
                print("Results to compare:       ", comparison_line[0:-1])
                print("Goool!!!")
            except AssertionError:
                print("My results:               ", numbers[0:-1])
                print("Results to compare:       ", comparison_line[0:-1])
                print("AssertionError: results don't match.")
            except IndexError:
                print("IndexError: number of operands less than expected.")
                print("Given input:", operand_line[0:-1])
            except ValueError:
                print("ValueError: only numeric input is accepted.")
                print("Given input:", operand_line[0:-1])
            except ZeroDivisionError:
                print("ZeroDivisionError: You can’t divide by 0.")
                print("Given input:", operand_line[0:-1])
            except Exception:
                print("kaBOOM: run for your life.")
        else:
            break
finally:
    print("˜ Game Over ˜")