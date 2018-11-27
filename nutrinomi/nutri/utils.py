

def list_of_lists(stats, stats_count):
    if not stats:
        return None
    objects = []
    for i in stats:
        if not objects:
            objects.append('Cita')
            objects.append('harris')
            objects.append('Mifflin')
            objects.append('valencia')
        else:
            objects.append(str(i.timestamp.date()))
            objects.append(i.harris)
            objects.append(i.miffin)
            objects.append(i.valencia)
    return split(objects, 4)


def split(objects, size):
    arrs = []
    while len(objects) > size:
        pice = objects[:size]
        arrs.append(pice)
        objects = objects[size:]
    arrs.append(objects)
    return arrs
