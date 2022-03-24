count = int(input())
base_list = []
for i in range(count):
    base_list.append([i for i in input().split(';')])
# base_list = [['Спартак', '9', 'Зенит', '10'], ['Локомотив', '12', 'Зенит', '3'], ['Спартак', '8', 'Локомотив', '15']]
base_dict = {}
for list in base_list:
    for elem in list[::2]:
        if elem not in base_dict:
            base_dict.update({elem: [0, 0, 0, 0, 0]})
        else:
            continue
for list in base_list:
    command1 = list[0]
    command2 = list[2]
    goal1 = int(list[1])
    goal2 = int(list[3])
    if goal1 > goal2:
        base_dict[command1][0] += 1
        base_dict[command1][1] += 1
        base_dict[command1][4] += 3

        base_dict[command2][0] += 1
        base_dict[command2][3] += 1

    elif goal1 < goal2:
        base_dict[command1][0] += 1
        base_dict[command1][3] += 1

        base_dict[command2][0] += 1
        base_dict[command2][1] += 1
        base_dict[command2][4] += 3

    else:
        base_dict[command1][0] += 1
        base_dict[command2][0] += 1
        base_dict[command1][2] += 1
        base_dict[command2][2] += 1
        base_dict[command1][4] += 1
        base_dict[command2][4] += 1

for key, values in base_dict.items():
    print(key + ':', *values)
