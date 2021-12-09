import converter_functions as conv_f


def calculate_rate(mode, report, middle):
    l = [int(bit >= middle) for bit in report] if (
        mode == 'gamma') else [int(bit < middle) for bit in report]

    return conv_f.convert_int_list_to_str(l)


def calculate_rating(mode, report):
    i = 0

    rate_mode = 'gamma' if (mode == 'oxygen_generator') else 'epsilon'

    while len(report) > 1:
        report_sum = list(map(sum, zip(*report)))
        rate = calculate_rate(rate_mode, report_sum, len(report)/2)
        report = list(filter(lambda x: x[i] == int(rate[i]), report))
        i += 1

    return conv_f.convert_int_list_to_str(report[0])


def calculate_bingo_score(board, mask):
    score = 0

    for i in range(5):
        for j in range(5):
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
