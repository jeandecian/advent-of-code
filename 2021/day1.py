import data_functions as data_f
import display_functions as disp_f


def count_increment(measures, window_size=1):
    window_measures = [sum(measures[i-(window_size-1):i+1])
                       for i in range(window_size-1, len(measures))]

    counter = 0

    for i in range(1, len(window_measures)):
        if (window_measures[i-1] < window_measures[i]):
            counter += 1

    return counter


measures = data_f.read_as_int(1)
disp_f.display_part(1, count_increment(measures))
disp_f.display_part(2, count_increment(measures, 3))
