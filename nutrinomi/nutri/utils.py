

def list_of_lists(stats, stats_count):
    if not stats:
        return None
    objects = []
    for i in stats:
        objects.append(i.id)
        objects.append(i.timestamp)
        objects.append(i.harris)
        objects.append(i.miffin)
        objects.append(i.valencia)
    return split(objects, 5)


def split(objects, size):
    arrs = []
    while len(objects) > size:
        pice = objects[:size]
        arrs.append(pice)
        objects = objects[size:]
    arrs.append(objects)
    return arrs
