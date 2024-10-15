def add(list, item):
    return list + [item]


def remove(list, item):
    new_list = []
    for i in list:
        if i != item:
            new_list = add(new_list, i)
    return new_list
