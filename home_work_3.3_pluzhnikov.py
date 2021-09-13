def thesaurus (*args):
    my_dict = {}
    for i in sorted(args):
        mail = i[0]
        if mail in my_dict:
            my_dict[mail] += [i]
        else:
            my_dict[mail] = [i]
    return my_dict
print (thesaurus ("Идрак", "Владимир", "Алексей", "Наталья", "Максим", "Илья", "Константин", "Петр"))