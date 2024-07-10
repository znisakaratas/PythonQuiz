import sys
message_order = list()
code_list = list()
final_code = list()
code_set = set()

def message():
    for j in range(len(line)):
        message_str = ""
        message_input = line[j][0:-1].split("\t")
        message_order.append(message_input)
        message_order.sort()
        code_list.append(message_input[0])
        code_set = set(code_list)
        final_code = list(code_set)
        final_code.sort()
    for j in range(len(final_code)):
        message_str += f"Message {j+1}\n"
        for i in range(len(message_order)):
            if message_order[i][0] == final_code[j]:
                message_str += f"{message_order[i][0]}\t{message_order[i][1]}\t{message_order[i][2]}\n"
    return output_f.write(message_str)

firstfile = sys.argv[1]
secondfile = sys.argv[2]
output_f = open(secondfile, "w", encoding="utf-8")
input_f = open(firstfile, "r", encoding="utf-8")
line = input_f.readlines()
message()
