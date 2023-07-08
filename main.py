from register import register_user, get_user_role
from data import Work

def run():
    users = register_user()
    username_parol = input("Введіть пароль (або введіть 'q' для виходу): ")
    if username_parol == 'q':
        return

    user_role = get_user_role(username_parol, users)
    if user_role is None:
        print("Немає такого паролю")
        return

    w = Work(user_role)
    while True:
        choice_method = input(
            'Виберіть метод: append for dict, append for tuple, popitem, pop, clear, items, values, keys, index, count: ')
        #w = Work(users)

        if choice_method == 'append for dict':
            w.append_dict()

        if choice_method == 'append for tuple':
            w.append_tuple()

        if choice_method == 'popitem':
            w.popitem()

        if choice_method == 'pop':
            w.pop()

        if choice_method == 'clear':
            w.clear()

        if choice_method == 'items':
            w.items()

        if choice_method == 'values':
            w.values()

        if choice_method == 'keys':
            w.keys()

        if choice_method == 'index':
            w.index()

        if choice_method == 'count':
            w.count()



#register_user()
run()