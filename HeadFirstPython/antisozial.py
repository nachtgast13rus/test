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


def average_age():
    global users
    count = 0
    for name in users:
        user = users[name]
        count += user["Age"]
    print(f"Average age is {count / len(users)}")


def count_min_friends():
    global users
    max_friends = 1000
    for friend in users:
        user = users[friend]
        friends = user["Friends"]
        if len(friends) < max_friends:
            max_friends = len(friends)
            most_antisocial = friend
    print(most_antisocial)


users = {}
while True:
    choice = input("Press 1 to add new user ")
    if choice == "1":
        add_user()
    else:
        break
average_age()
count_min_friends()
