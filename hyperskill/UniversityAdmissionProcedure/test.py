def create_student_list(en_list, amo_unt, faculty):
    faculty_list = []
    i = 0
    while i < len(en_list):
        if en_list[i][3] == faculty and len(faculty_list) < amo_unt and len(en_list) != 0:
            faculty_list.append(en_list[i])
            del en_list[i]
        else:
            i += 1
    return faculty_list


def add_student(en_list, faculty_list, amo_unt, faculty, index):
    i = 0
    while i < len(en_list):
        if en_list[i][index] == faculty and len(faculty_list) < amo_unt and len(en_list) != 0:
            faculty_list.append(en_list[i])
            del en_list[i]
        else:
            i += 1
    return faculty_list

def print_applicants(faculty, faculty_list):
    print(faculty)
    for i in faculty_list:
        print(*i[:3])
    print()


with open("test.txt", 'r', encoding="utf-8") as file:
    applicants_list = [line.strip().split() for line in file]
amount = int(input())
applicants_list.sort(key=lambda x: (x[3], -float(x[2])))
biotech_list = create_student_list(en_list=applicants_list, amo_unt=amount, faculty="Biotech")
chemistry_list = create_student_list(en_list=applicants_list, amo_unt=amount, faculty="Chemistry")
engineering_list = create_student_list(en_list=applicants_list, amo_unt=amount, faculty="Engineering")
mathematics_list = create_student_list(en_list=applicants_list, amo_unt=amount, faculty="Mathematics")
physics_list = create_student_list(en_list=applicants_list, amo_unt=amount, faculty="Physics")
applicants_list.sort(key=lambda x: (x[4], -float(x[2])))
biotech_list = add_student(en_list=applicants_list,
                           faculty_list=biotech_list, amo_unt=amount, faculty="Biotech", index=4)
chemistry_list = add_student(en_list=applicants_list,
                             faculty_list=chemistry_list, amo_unt=amount, faculty="Chemistry", index=4)
engineering_list = add_student(en_list=applicants_list,
                               faculty_list=engineering_list, amo_unt=amount, faculty="Engineering", index=4)
mathematics_list = add_student(en_list=applicants_list,
                               faculty_list=mathematics_list, amo_unt=amount, faculty="Mathematics", index=4)
physics_list = add_student(en_list=applicants_list,
                           faculty_list=physics_list, amo_unt=amount, faculty="Physics", index=4)
applicants_list.sort(key=lambda x: (x[5], -float(x[2])))
biotech_list = add_student(en_list=applicants_list,
                           faculty_list=biotech_list, amo_unt=amount, faculty="Biotech", index=5)
chemistry_list = add_student(en_list=applicants_list,
                             faculty_list=chemistry_list, amo_unt=amount, faculty="Chemistry", index=5)
engineering_list = add_student(en_list=applicants_list,
                               faculty_list=engineering_list, amo_unt=amount, faculty="Engineering", index=5)
mathematics_list = add_student(en_list=applicants_list,
                               faculty_list=mathematics_list, amo_unt=amount, faculty="Mathematics", index=5)
physics_list = add_student(en_list=applicants_list,
                           faculty_list=physics_list, amo_unt=amount, faculty="Physics", index=5)
print_applicants(faculty="Biotech", faculty_list=biotech_list)
print_applicants(faculty="Chemistry", faculty_list=chemistry_list)
print_applicants(faculty="Engineering", faculty_list=engineering_list)
print_applicants(faculty="Mathematics", faculty_list=mathematics_list)
print_applicants(faculty="Physics", faculty_list=physics_list)