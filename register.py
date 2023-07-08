
def register_user():
    users = {
        'user': 'user',
        'nastia': 'nastia',
    }
    return users


def get_user_role(username_parol, users):
    if username_parol in users:
        return users[username_parol]
    else:
        return None















#def register_user():
    #users = {'admin': [], 'user': []}
    #while True:
        #username = input("Введіть ім'я користувача (або введіть 'q' для виходу): ")
        #if username == 'q':
            #break

        #role = input("Виберіть роль (admin/user) для користувача '{}': ".format(username))
        #if role not in ['admin', 'user']:
            #print("Недійсна роль. Будь ласка, виберіть admin або user.")
            #continue

        #users[role].append(username)
        #print("Користувач '{}'' успішно зареєстрований з роллю '{}'\n".format(username, role))

    #return users

