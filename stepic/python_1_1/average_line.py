student_list = []
with open('dataset3.txt', 'r', encoding='utf-8') as file:
    for line in file:
        student_list += [[i for i in line.split()]]
student_dict = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [], '11': []}
for line in student_list:
    student_dict[line[0]] += [int(line[2])]
with open('dataset3_output.txt', 'w', encoding='utf-8') as file:
    for elem in student_dict:
        if len(student_dict[elem]) != 0:
            average = sum(student_dict[elem]) / len(student_dict[elem])
            file.write(elem + ' ' + str(average) + '\n')
        else:
            file.write(elem + ' - ' + '\n')
