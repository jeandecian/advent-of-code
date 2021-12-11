import constants as c


def calculate_rate(mode, report, middle):
    l = [int(bit >= middle) for bit in report] if (
        mode == 'gamma') else [int(bit < middle) for bit in report]

    return convert_int_list_to_str(l)


def calculate_rating(mode, report):
    i = 0

    rate_mode = c.GAMMA if (mode == c.OXYGEN_GENERATOR) else c.EPSILON

    while len(report) > 1:
        report_sum = list(map(sum, zip(*report)))
        rate = calculate_rate(rate_mode, report_sum, len(report)/2)
        report = list(filter(lambda x: x[i] == int(rate[i]), report))
        i += 1

    return convert_int_list_to_str(report[0])


def calculate_bingo_score(board, mask):
    score = 0

    for i in range(c.BINGO_BOARD_SIZE):
        for j in range(c.BINGO_BOARD_SIZE):
            if (mask[i][j] == 0):
                score += board[i][j]

    return score


def calculate_lines_overlap(diagram):
    count = 0

    for row in diagram:
        for col in row:
            if (col > 1):
                count += 1

    return count


def convert_int_list_to_str(l):
    return "".join(list(map(str, l)))


def convert_entry_to_point(entry):
    return list(map(int, entry.split(',')))


def create_empty_matrix(width, height):
    return [[0 for x in range(width)] for y in range(height)]


def create_empty_matrices(nb_matrices, width, height):
    return [[[0 for x in range(width)] for y in range(height)] for z in range(nb_matrices)]


def display_part(part, answer):
    print(f"[{part}] {answer}")


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


def read_data(day, mode):
    with open(f"{c.DATA_PATH}{mode}/{mode}{day}.txt", "r") as infile:
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


def read_as_int_list(day, mode='input'):
    return list(map(int, read_as_str(day, mode)[0].split(',')))
