import utils


def count_increment(measures, window_size=1):
    window_measures = [sum(measures[i-(window_size-1):i+1])
                       for i in range(window_size-1, len(measures))]

    counter = 0

    for i in range(1, len(window_measures)):
        if (window_measures[i-1] < window_measures[i]):
            counter += 1

    return counter


if __name__ == '__main__':
    measures = utils.read_as_int(1)
    utils.display_part(1, count_increment(measures))
    utils.display_part(2, count_increment(measures, 3))
