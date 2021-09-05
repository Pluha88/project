spisok = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_spisok = []
for i in new_spisok:
    if i.replace("+","").replace("-","").isdigit():
        if i.isdigit():
            new_spisok.append(f"'{int(i):02}'")
        else:
            new_spisok.append(f"'{i[0]}{int(i[1:]):02}'")
spisok = " ".join(['в', '"05"', 'часов', '"17"', 'минут', 'температура', 'воздуха', 'была', '"+05"', 'градусов'])
print(spisok)
