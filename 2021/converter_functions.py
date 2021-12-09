def convert_int_list_to_str(l):
    return "".join(list(map(str, l)))


def convert_entry_to_point(entry):
    return list(map(int, entry.split(',')))
