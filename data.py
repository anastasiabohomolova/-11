class Work:

    def __init__(self, user_type):
        self.dict_t = {'name': 'Mary', 'food': 'junk food', 'dog': 'Tao', 'age': 21}
        self.tuple_e = (1, 1, 1, 'salary', 'salary', 'name', 32323, 'home')
        self.user_type = user_type

    def append_dict(self):
        if self.user_type != 'nastia':
            print("Доступ заборонено для простого користувача.")
            return
        el = input('виберіть: item, key, value : ')
        if el == 'key':
            k = input('напишіть ключ: ')
            for key in self.dict_t.keys():
                if k == key:
                    etap = input('такий ключ вже є, міняємо його на новий? yes or no: ')
                    if etap == 'yes':
                        new_k = input('напишіть новий ключ: ')
                        self.dict_t[new_k] = self.dict_t[key]
                        del self.dict_t[key]
                        print(self.dict_t)

                    elif etap == 'no':
                        nv = input('міняємо значення(value) для ключа, напишіть нове value: ')
                        self.dict_t[k] = nv
                        print(self.dict_t)
                        break
                elif k != key:
                    val = input('напишіть нове value для key: ')
                    self.dict_t[k] = val
                    print(self.dict_t)
                    break

        elif el == 'value':
            v = input('напишіть значення: ')
            for key, value in self.dict_t.items():
                if v == value:
                    etap = input('таке value вже є, міняємо на нове? yes or no: ')
                    if etap == 'yes':
                        new_v = input('напишіть нове значення: ')
                        self.dict_t[key] = new_v
                        print(self.dict_t)
                    elif etap == 'no':
                        newk = input('напишіть новий ключ для значення: ')
                        self.dict_t[newk] = v
                        print(self.dict_t)
                        break
                elif v != value:
                    newk = input('напишіть ключ для значення: ')
                    self.dict_t[newk] = v
                    print(self.dict_t)
                    break

        elif el == 'item':
            new_k = input('Напишіть ключ: ')
            new_v = input('Напишіть значення: ')
            for items in self.dict_t.items():
                if new_k and new_v != items:
                    item = self.dict_t.setdefault(new_k, new_v)
                    print(self.dict_t)
                elif new_k == items and new_v == items:
                    print('Такі елементи вже є')
                break

    def append_tuple(self):
        if self.user_type != 'nastia':
            print("Доступ заборонено для простого користувача.")
            return
        add_el = input('Виберіть тип даних str or int: ')
        if add_el == 'int':
            n_int = int(input('напишіть int: '))
            new_t = self.tuple_e + (n_int, )
            print(new_t)
        elif add_el == 'str':
            n_str = input('напишіть str:' )
            new_t = self.tuple_e + (n_str, )
            print(new_t)

    def popitem(self):
        p_it = self.dict_t.popitem()
        print(p_it)

    def pop(self):
        k = input('Напишіть ключ: ')
        p_op = self.dict_t.pop(k)
        print(p_op)

    def clear(self):
        clr = self.dict_t.clear()
        print(clr)

    def items(self):
        i_tms = self.dict_t.items()
        print(i_tms)

    def values(self):
        v_es = self.dict_t.values()
        print(v_es)

    def keys(self):
        k_ys = self.dict_t.keys()
        print(k_ys)

    def index(self):
        el = input('Виберіть int or str: ')
        if el == 'int':
            vubir = int(input('напишіть int: '))
            ind = self.tuple_e.index(vubir)
            print(ind)
        elif el == 'str':
            vubir_2 = str(input('напишіть str: '))
            ix = self.tuple_e.index(vubir_2)
            print(ix)

    def count(self):
        ch = input('Виберіть int or str: ')
        if ch == 'int':
            number = int(input('напишіть int: '))
            c_nt = self.tuple_e.count(number)
            print(c_nt)
        elif ch == 'str':
            element = input('напишіть str: ')
            c_nt = self.tuple_e.count(element)
            print(c_nt)









