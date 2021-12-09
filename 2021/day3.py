import constants as c
import utils


def part1(report):
    report_sum = list(map(sum, zip(*report)))

    middle = len(report)/2
    gamma_rate = int(utils.calculate_rate(c.GAMMA, report_sum, middle), 2)
    epsilon_rate = int(utils.calculate_rate(c.EPSILON, report_sum, middle), 2)

    return gamma_rate * epsilon_rate


def part2(report):
    oxygen_generator_rating = int(
        utils.calculate_rating(c.OXYGEN_GENERATOR, report), 2)
    CO2_scrubber_rating = int(
        utils.calculate_rating('CO2_scrubber', report), 2)

    return oxygen_generator_rating * CO2_scrubber_rating


if __name__ == '__main__':
    diagnostics = utils.read_as_str(3)
    report = list(map(lambda x: list(map(int, list(x.rstrip()))), diagnostics))
    utils.display_part(1, part1(report))
    utils.display_part(2, part2(report))
