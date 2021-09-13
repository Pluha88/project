d = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
     'four': 'четыре', 'five': 'пять', 'six': 'шесть',
     'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
def num_translate(word):
    if word.istitle():
        return str(d.get(word.lower())).title()
    return d.get(word)

print(num_translate(input("Введите ваше число: ")))