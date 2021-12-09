import utils


def part1(movements):
    horizontal, depth = 0, 0

    for movement in movements:
        units = int(movement[1])

        if (movement[0] == 'forward'):
            horizontal += units
        elif (movement[0] == 'down'):
            depth += units
        elif (movement[0] == 'up'):
            depth -= units

    return horizontal * depth


def part2(movements):
    horizontal, depth, aim = 0, 0, 0

    for movement in movements:
        units = int(movement[1])

        if (movement[0] == 'forward'):
            horizontal += units
            depth += aim * units
        elif (movement[0] == 'down'):
            aim += units
        elif (movement[0] == 'up'):
            aim -= units

    return horizontal * depth


if __name__ == '__main__':
    movements = utils.read_as_list(2)
    utils.display_part(1, part1(movements))
    utils.display_part(2, part2(movements))
