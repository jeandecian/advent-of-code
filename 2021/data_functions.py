DATA_PATH = 'data/'


def read_data(day, mode):
    with open(f"{DATA_PATH}{mode}/{mode}{day}.txt", "r") as infile:
        data = infile.readlines()

    infile.close()

    return data


def read_as_int(day, mode='input'):
    return list(map(int, read_data(day, mode)))


def read_as_list(day, mode='input'):
    return list(map(lambda x: x.split(), read_data(day, mode)))


def read_as_str(day, mode='input'):
    return list(map(str, read_data(day, mode)))
