import utils


def count_octopus_flashes(energy_levels, y, x, flashes_mask):
    if (energy_levels[y][x] <= 9 or flashes_mask[y][x] == 1):
        return 0

    flashes_count = 0

    flashes_mask[y][x] = 1
    flashes_count += 1

    if (x > 0):
        energy_levels[y][x-1] += 1
        flashes_count += count_octopus_flashes(
            energy_levels, y, x-1, flashes_mask)

    if (x < 9):
        energy_levels[y][x+1] += 1
        flashes_count += count_octopus_flashes(
            energy_levels, y, x+1, flashes_mask)

    if (y > 0):
        energy_levels[y-1][x] += 1
        flashes_count += count_octopus_flashes(
            energy_levels, y-1, x, flashes_mask)

    if (y < 9):
        energy_levels[y+1][x] += 1
        flashes_count += count_octopus_flashes(
            energy_levels, y+1, x, flashes_mask)

    if (x > 0 and y > 0):
        energy_levels[y-1][x-1] += 1
        flashes_count += count_octopus_flashes(
            energy_levels, y-1, x-1, flashes_mask)

    if (x < 9 and y > 0):
        energy_levels[y-1][x+1] += 1
        flashes_count += count_octopus_flashes(
            energy_levels, y-1, x+1, flashes_mask)

    if (x > 0 and y < 9):
        energy_levels[y+1][x-1] += 1
        flashes_count += count_octopus_flashes(
            energy_levels, y+1, x-1, flashes_mask)

    if (x < 9 and y < 9):
        energy_levels[y+1][x+1] += 1
        flashes_count += count_octopus_flashes(
            energy_levels, y+1, x+1, flashes_mask)

    return flashes_count


def part1(energy_levels):
    size = 10

    flashes_count = 0

    for _ in range(100):
        flashes_mask = utils.create_empty_matrix(size, size)
        energy_levels = [[x + 1 for x in y] for y in energy_levels]

        for y in range(size):
            for x in range(size):
                flashes_count += count_octopus_flashes(
                    energy_levels, y, x, flashes_mask)

        for y in range(size):
            for x in range(size):
                if (energy_levels[y][x] > 9):
                    energy_levels[y][x] = 0

    return flashes_count


def part2(energy_levels):
    size = 10

    synchronized_flashes = utils.create_empty_matrix(size, size)

    steps = 0

    while(synchronized_flashes != energy_levels):
        flashes_mask = utils.create_empty_matrix(size, size)
        energy_levels = [[x + 1 for x in y] for y in energy_levels]

        for y in range(size):
            for x in range(size):
                count_octopus_flashes(energy_levels, y, x, flashes_mask)

        for y in range(size):
            for x in range(size):
                if (energy_levels[y][x] > 9):
                    energy_levels[y][x] = 0

        steps += 1

    return steps


if __name__ == '__main__':
    energy_levels = utils.read_as_str(11)
    energy_levels = [list(map(int, list(str(energy_row.rstrip()))))
                     for energy_row in energy_levels]
    utils.display_part(1, part1(energy_levels))
    utils.display_part(2, part2(energy_levels))
