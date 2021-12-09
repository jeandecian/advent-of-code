def find_max_point(vent):
    return max(vent, key=lambda x: x[1])[1], max(vent, key=lambda x: x[0])[0]


def find_max_vents(vents):
    max_vents = []

    for vent in vents:
        max_vents.append([*find_max_point(vent)])

    return find_max_point(max_vents)


def find_vertical_line_min_max(vent):
    return min(vent, key=lambda x: x[1])[1], max(vent, key=lambda x: x[1])[1]


def find_horizontal_line_min_max(vent):
    return min(vent, key=lambda x: x[0])[0], max(vent, key=lambda x: x[0])[0]
