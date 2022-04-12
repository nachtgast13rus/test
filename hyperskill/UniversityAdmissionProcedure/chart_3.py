applicants = int(input())
accepted = int(input())
applicants_list = [input().split() for x in range(applicants)]
applicants_list.sort(key=lambda x: (-float(x[2]), x[0]))
print("Successful applicants:")
for x in range(accepted):
    print(applicants_list[x][0], applicants_list[x][1])

