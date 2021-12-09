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


def read_as_line_matrices(day, mode='input'):
    raw_data = read_as_list(day, mode)
    draw = list(map(int, raw_data[0][0].split(',')))
    nb_boards = (len(raw_data) - 1) // 6

    boards = []

    for i in range(nb_boards):
        boards.append(
            list(map(lambda x: list(map(int, x)), raw_data[6*i+2:6*i+7])))

    return draw, boards
