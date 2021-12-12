import utils


def part1(signals):
    easy_digits_segments = [2, 3, 4, 7]

    count = 0

    for signal in signals:
        output = signal[11:]
        for digit in output:
            if (len(digit) in easy_digits_segments):
                count += 1

    return count


def part2(signals):
    count = 0

    for signal in signals:
        digits_signals = ['' for _ in range(10)]

        input_signals = signal[0:10]
        for i in range(len(input_signals)):
            input_signals[i] = ''.join(sorted(list(input_signals[i])))

        sorted_input_signals = sorted(input_signals, key=len)
        digits_signals[1] = sorted_input_signals[0]
        digits_signals[4] = sorted_input_signals[2]
        digits_signals[7] = sorted_input_signals[1]
        digits_signals[8] = sorted_input_signals[9]

        sorted_input_signals_five = sorted_input_signals[3:6]
        sorted_input_signals_six = sorted_input_signals[6:9]

        digits_signals[9] = list(filter(lambda x, subset=digits_signals[4]: set(
            subset).issubset(set(x)), sorted_input_signals_six))[0]
        sorted_input_signals_six.remove(digits_signals[9])

        digits_signals[0] = list(filter(lambda x, subset=digits_signals[7]: set(
            subset).issubset(set(x)), sorted_input_signals_six))[0]
        sorted_input_signals_six.remove(digits_signals[0])

        digits_signals[6] = sorted_input_signals_six[0]

        digits_signals[3] = list(filter(lambda x, subset=digits_signals[7]: set(
            subset).issubset(set(x)), sorted_input_signals_five))[0]
        sorted_input_signals_five.remove(digits_signals[3])

        digits_signals[5] = list(filter(lambda x, subset=digits_signals[6]: set(
            x).issubset(set(subset)), sorted_input_signals_five))[0]
        sorted_input_signals_five.remove(digits_signals[5])

        digits_signals[2] = sorted_input_signals_five[0]

        output = []
        output_signals = signal[11:]
        for digit in output_signals:
            sorted_digit = ''.join(sorted(list(digit)))
            output.append(str(digits_signals.index(sorted_digit)))

        count += int(''.join(output))

    return count


if __name__ == '__main__':
    signals = utils.read_as_list(8)
    utils.display_part(1, part1(signals))
    utils.display_part(2, part2(signals))
