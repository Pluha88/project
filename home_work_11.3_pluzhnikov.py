class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения списка: '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение!")
                variant = input(f'Попробовать еще раз? Да/Нет ')
                if variant == 'Да' and variant == 'Да':
                    val = int(input('Введите значения списка: '))
                    self.my_list.append(val)
                    print(f'Текущий список - {self.my_list} \n ')
                elif variant == 'Нет' or variant == 'Нет':
                    return f'До скороой встречи!'
                else:
                    return f'До скороой встречи!'

try_except = Error()
print(try_except.my_input())
