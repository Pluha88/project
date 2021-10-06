
d = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
     'four': 'четыре', 'five': 'пять', 'six': 'шесть',
     'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
num_translate = input(" Введите ваше число для перевода: ")
for i in d:
    if num_translate in i:
        print(d.get(i))
else:
    print("Число введено неправильно")




