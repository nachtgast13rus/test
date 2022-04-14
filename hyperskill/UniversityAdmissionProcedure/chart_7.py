with open('applicants.txt', 'r', encoding='utf-8') as file:
    applicants = file.read()


def score_checker(score1, score2):
    if score1 > score2:
        return score1
    elif score2 > score1:
        return score2
    elif score2 == score1:
        return score2


successful = int(input())

clean_list = []
for applicant in applicants.split('\n'):
    name, surname, physics, chemistry, math, computer_science, special, choice1, choice2, choice3 = applicant.split()
    priorities = {
        'Physics': score_checker((float(physics) + float(math))/2, float(special)),
        'Chemistry': score_checker(float(chemistry), float(special)),
        'Mathematics': score_checker(float(math), float(special)),
        'Engineering': score_checker((float(computer_science) + float(math))/2, float(special)),
        'Biotech': score_checker((float(chemistry) + float(physics))/2, float(special))
    }
    for preference, choice in enumerate([choice1, choice2, choice3], start=1):
        clean_list.append([name + ' ' + surname, preference, priorities[choice], choice])
ordered_list = sorted(clean_list, key=lambda x: [x[1], -x[2], x[0], x[3]])
approved = {choice: {} for choice in sorted([applicant[-1] for applicant in ordered_list])}
processed = []
for name, preference, result, choice in ordered_list:
    if name not in processed and len(approved[choice]) < successful:
        if choice not in approved:
            approved[choice] = {name: result}
        else:
            approved[choice][name] = result
        processed.append(name)
for choice, approved in sorted(approved.items(), key=lambda x: [x[0], x[1]]):
    print(choice)
    with open(choice + '.txt', 'w') as output:
        for name, result in sorted(approved.items(), key=lambda x: [-x[1], x[0]]):
            print(name,  result)
            output.write(name + ' ' + str(result) + '\n')
        print()
