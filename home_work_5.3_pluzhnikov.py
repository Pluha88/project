from itertools import islice, zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Андрей']
klasses = ['9A', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9A']

result = (i for i in zip_longest(tutors, klasses) if len(tutors) > len(klasses))
print(type(result))
print(*islice(result, int(input("Введите запрашиваемую длину списка: "))))
