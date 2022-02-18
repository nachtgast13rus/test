def add_user():
    global users
    name = input("Press name of a new user ")
    age = int(input("Press age of a new user "))
    email = input("Press email of a new user ")
    sex = input("Press sex of a new user ")
    friends = list()
    while True:
        friends_name = input("Press name of user`s friend or 'n' to continue... ")
        if friends_name == 'n':
            break
        else:
            friends.append(friends_name)
    attributes = {"Age": age, "Email": email, "Sex": sex, "Friends": friends}
    users[name] = attributes


users = {}
choice = input("Press 1 to add new user ")
if choice == "1":
    add_user()
count = 0
for name in users:
    user = users[name]
    count += user["Age"]
print(count)
