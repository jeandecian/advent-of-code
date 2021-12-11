import utils


def calculate_lanterfishes_propagation(ages, day):
    counter = utils.create_counter_list(ages, 0, 9)

    for _ in range(day):
        temp_6 = 0
        temp_8 = 0
        for i in range(len(counter)-1):
            if (i == 0):
                temp_6 = counter[i]
                temp_8 = counter[i]

            counter[i] = counter[i+1]

        counter[6] += temp_6
        counter[8] = temp_8

    return sum(counter)


if __name__ == '__main__':
    lanterfishses_ages = utils.read_as_int_list(6)
    utils.display_part(
        1, calculate_lanterfishes_propagation(lanterfishses_ages, 80))
    utils.display_part(
        2, calculate_lanterfishes_propagation(lanterfishses_ages, 256))
