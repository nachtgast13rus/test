users = {"Evgen": {"Age": 40, "Email": "evgen@mail.ru", "Sex": "m", "Friends": ["Kobzon", "Sosok", "Puhlya"]},
         "Sosok": {"Age": 45, "Email": "sosok@mail.ru", "Sex": "m", "Friends": ["Kobzon", "Evgen", "Puhlya", "Yujni"]},
         "Puhlya": {"Age": 42, "Email": "puhlya@mail.ru", "Sex": "m", "Friends": ["Kobzon", "Sosok"]}}

max_friends = 1000
for friend in users:
    user = users[friend]
    friends = user["Friends"]
    if len(friends) < max_friends:
        max_friends = len(friends)
        most_antisocial = friend
print(most_antisocial)
