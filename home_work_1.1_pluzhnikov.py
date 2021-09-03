duration = int(input('Введите ваши секунды для конвертирования: '))
s = 60
m = 60 * s
h = 24 * m
d = h * 31
days = 24
prop = (s * 1)/100
if duration < s:
    print(f'{duration} sec')
elif duration >= s and duration < m:
    duration = (duration * s) / m
    duration1 = int(duration)
    print(f'{duration1} min')
    dur = duration - duration1
    dur = round(dur * s)
    print(f'{dur} sec')
elif duration >= m and duration < h:
    duration = (duration / m)
    duration1 = round(duration)
    print(f'{duration1} hour')
    dur = duration - duration1
    dur1 = round(dur * s)
    dur2 = (dur * s)
    print(f'{dur1} min')
    dur = dur2 - dur1
    dur = round(dur * s)
    print(f'{dur} sec')
elif duration >= h and duration < d:
    duration = (duration / h)
    duration1 = int(duration)
    print(f'{duration1} days')
    dur = duration - duration1
    dur1 = round(dur * days)
    dur2 = (dur * days)
    print(f'{dur1} hour')
    dur = dur2 - dur1
    dur3 = round(dur * s)
    print(f'{dur3} min')
    dur = dur * s
    dur = round(((dur - dur3)*prop) * 100)
    print(f'{dur} sec')
# Выше я привожу пример как я сам изначально решил, я долго мучал но в итоге код работает не коректно

# Ниже, понятное дело, привожу как оно и должно быть
# duration = int(input('Введите ваше число: '))
# s = duration % 60
# m = (duration // 60) % 60
# h = (duration // 3600) % 24
# d = (duration // 86400) % 30
# month = duration // 2592000
# print(month, 'месяц', d, 'дней', h, 'час', m, 'мин', s, 'сек')

