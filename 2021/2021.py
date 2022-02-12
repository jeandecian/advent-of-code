import unittest
import utils
import day1
import day2
import day3
import day4
import day5
import day6
import day7
import day8
import day9


class Test2021(unittest.TestCase):
    def test_day1(self):
        measures = utils.read_as_int(1)
        self.assertEqual(day1.count_increment(measures), 1477)
        self.assertEqual(day1.count_increment(measures, 3), 1523)

    def test_day2(self):
        movements = utils.read_as_list(2)
        self.assertEqual(day2.part1(movements), 1936494)
        self.assertEqual(day2.part2(movements), 1997106066)

    def test_day3(self):
        diagnostics = utils.read_as_str(3)
        report = list(
            map(lambda x: list(map(int, list(x.rstrip()))), diagnostics))
        self.assertEqual(day3.part1(report), 2261546)
        self.assertEqual(day3.part2(report), 6775520)

    def test_day4(self):
        draw, boards = utils.read_as_line_matrices(4)
        self.assertEqual(day4.part1(draw, boards), 74320)
        self.assertEqual(day4.part2(draw, boards), 17884)

    def test_day5(self):
        vents = utils.read_as_list(5)
        vents = [[utils.convert_entry_to_point(
            vent[0]), utils.convert_entry_to_point(vent[2])] for vent in vents]
        self.assertEqual(day5.part1(vents), 6461)
        self.assertEqual(day5.part2(vents), 18065)

    def test_day6(self):
        lanterfishses_ages = utils.read_as_int_list(6)
        self.assertEqual(day6.calculate_lanterfishes_propagation(
            lanterfishses_ages, 80), 359999)
        self.assertEqual(day6.calculate_lanterfishes_propagation(
            lanterfishses_ages, 256), 1631647919273)

    def test_day7(self):
        crabs_positions = utils.read_as_int_list(7)
        self.assertEqual(day7.calculate_min_fuel(crabs_positions, 1), 356179)
        self.assertEqual(day7.calculate_min_fuel(crabs_positions, 2), 99788435)

    def test_day8(self):
        signals = utils.read_as_list(8)
        self.assertEqual(day8.part1(signals), 237)
        self.assertEqual(day8.part2(signals), 1009098)

    def test_day9(self):
        heightmap = utils.read_as_str(9)
        heightmap = [list(map(int, list(str(height.rstrip()))))
                     for height in heightmap]
        self.assertEqual(day9.part1(heightmap), 562)
        self.assertEqual(day9.part2(heightmap), 1076922)


if __name__ == '__main__':
    unittest.main()
