for i in range(1, 101):
    if i <= 1:
        print(f'{i} процент')
    elif 1 < i <= 4:
        print(f'{i} процента')
    elif 4 < i <= 20:
        print(f'{i} процентов')
    elif i <= 21:
        print(f'{i} процент')
    elif 21 < i <= 24:
        print(f'{i} процента')
    elif 24 < i <= 30:
        print(f'{i} процентов')
    elif i <= 31:
        print(f'{i} процент')
    elif 31 < i <= 34:
        print(f'{i} процента')
    elif 34 < i <= 40:
        print(f'{i} процентов')
    elif i <= 41:
        print(f'{i} процент')
    elif 41 < i <= 44:
        print(f'{i} процента')
    elif 44 < i <= 50:
        print(f'{i} процентов')
    elif i <= 51:
        print(f'{i} процент')
    elif 51 < i <= 54:
        print(f'{i} процента')
    elif 54 < i <= 60:
        print(f'{i} процентов')
    elif i <= 61:
        print(f'{i} процент')
    elif 61 < i <= 64:
        print(f'{i} процента')
    elif 64 < i <= 70:
        print(f'{i} процентов')
    elif i <= 71:
        print(f'{i} процент')
    elif 71 < i <= 74:
        print(f'{i} процента')
    elif 74 < i <= 80:
        print(f'{i} процентов')
    elif i <= 81:
        print(f'{i} процент')
    elif 81 < i <= 84:
        print(f'{i} процента')
    elif 84 < i <= 90:
        print(f'{i} процентов')
    elif i <= 91:
        print(f'{i} процент')
    elif 91 < i <= 94:
        print(f'{i} процента')
    elif 94 < i <= 100:
        print(f'{i} процентов')
# Я не искал легких путей)

# Ниже приведен правильное решение
# for percent in range(101):
#    if percent % 10 == 1 and percent % 100 !=11:
#        print(percent, 'процент,', end=" ")
#    elif 1 < percent % 10 < 5 and not 11 < percent % 100 < 15:
#        print(percent, 'процента,', end=" ")
#    else:
#        print(percent, 'процентов,', end=" ")
