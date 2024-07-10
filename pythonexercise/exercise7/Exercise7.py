import sys


def check():
    name = line.split(":")
    for j in range(len(student_input)):
        try:
            if student_input[j] in name:
                output_file.write("Name:{},University: {}".format(student_input[j], name[1]))
            else:
                output_file.write("No record of {} is found.\n".format(student_input[j]))
        except:
            pass
    global should_stop
    should_stop = True

file_name = sys.argv[1]
file = open(file_name, "r", encoding="utf-8")
output_file = open("Student_output.txt", "w", encoding="utf-8")
should_stop = False
while not should_stop:
    line = file.readline()
    student_input = sys.argv[2:]
    check()
