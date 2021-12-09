import calculator_functions as calc_f
import data_functions as data_f
import display_functions as disp_f


def part1(report):
    report_sum = list(map(sum, zip(*report)))

    middle = len(report)/2
    gamma_rate = int(calc_f.calculate_rate('gamma', report_sum, middle), 2)
    epsilon_rate = int(calc_f.calculate_rate('epsilon', report_sum, middle), 2)

    return gamma_rate * epsilon_rate


def part2(report):
    oxygen_generator_rating = int(
        calc_f.calculate_rating('oxygen_generator', report), 2)
    CO2_scrubber_rating = int(
        calc_f.calculate_rating('CO2_scrubber', report), 2)

    return oxygen_generator_rating * CO2_scrubber_rating


if __name__ == '__main__':
    diagnostics = data_f.read_as_str(3)
    report = list(map(lambda x: list(map(int, list(x.rstrip()))), diagnostics))
    disp_f.display_part(1, part1(report))
    disp_f.display_part(2, part2(report))
