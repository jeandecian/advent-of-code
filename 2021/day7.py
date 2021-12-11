import utils


def calculate_min_fuel(positions, part):
    counter = utils.create_counter_list(
        positions, min(positions), max(positions)+1)

    fuel = []

    for i in range(len(counter)):
        fuel.append(utils.calculate_fuel(counter, i, part))

    return min(fuel)


if __name__ == '__main__':
    crabs_positions = utils.read_as_int_list(7)
    utils.display_part(1, calculate_min_fuel(crabs_positions, 1))
    utils.display_part(2, calculate_min_fuel(crabs_positions, 2))
