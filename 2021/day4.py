import calculator_functions as calc_f
import create_functions as crea_f
import data_functions as data_f
import display_functions as disp_f


def check_board_masks(board):
    for row in board:
        if (sum(row) == 5):
            return True

    if (5 in list(map(sum, zip(*board)))):
        return True

    return False


def part1(draw, boards):
    boards_masks = crea_f.create_empty_matrices(len(boards), 5, 5)
    bingo = False
    number_drawn = 0
    winning_board = 0
    current_draw = [d for d in draw]

    while not bingo:
        number_drawn = current_draw.pop(0)

        for i in range(len(boards)):
            temp_board_masks = list(
                map(lambda x: list(map(lambda x: int(x == number_drawn), x)), boards[i]))

            for j in range(5):
                boards_masks[i][j] = [
                    x + y for (x, y) in zip(boards_masks[i][j], temp_board_masks[j])]

            bingo = check_board_masks(boards_masks[i])
            if (bingo):
                winning_board = i
                break

    score = calc_f.calculate_bingo_score(
        boards[winning_board], boards_masks[winning_board])

    return score * number_drawn


def part2(draw, boards):
    boards_masks = crea_f.create_empty_matrices(len(boards), 5, 5)
    bingo = False
    number_drawn = 0
    last_winning_board = 0
    winning_boards_masks = [0 for i in range(len(boards))]
    current_draw = [d for d in draw]

    while not bingo:
        number_drawn = current_draw.pop(0)

        for i in range(len(boards)):
            temp_board_masks = list(
                map(lambda x: list(map(lambda x: int(x == number_drawn), x)), boards[i]))

            for j in range(5):
                boards_masks[i][j] = [
                    x + y for (x, y) in zip(boards_masks[i][j], temp_board_masks[j])]

            if (check_board_masks(boards_masks[i])):
                last_winning_board = i
                winning_boards_masks[i] = 1

                if (sum(winning_boards_masks) == len(boards)):
                    bingo = True
                    break

    score = calc_f.calculate_bingo_score(
        boards[last_winning_board], boards_masks[last_winning_board])

    return score * number_drawn


if __name__ == '__main__':
    draw, boards = data_f.read_as_line_matrices(4)
    disp_f.display_part(1, part1(draw, boards))
    disp_f.display_part(2, part2(draw, boards))
