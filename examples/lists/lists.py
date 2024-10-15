def add(list, item):
    return list + [item]


def remove(list, item):
    return [x for x in list if x != item]
