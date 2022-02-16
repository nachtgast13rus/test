import random

scopes_list = [random.randint(1, 100) for i in range(10)]
cost_list = [random.random() for k in range(10)]
first = 0
first_index = 0
second_index = 0
second = 0
for i in range(len(scopes_list)):
    print(f"Пузырьковый раствор №{i} - результат {scopes_list[i]} ")
first = sorted(scopes_list)[-1]
second = sorted(scopes_list)[-2]
print(f"Растворы с наилучшим результатом [{scopes_list.index(first)}, {scopes_list.index(second)}]")
print(cost_list)
