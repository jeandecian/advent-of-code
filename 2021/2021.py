import unittest
import converter_functions as conv_f
import data_functions as data_f
import day1
import day2
import day3
import day4
import day5


class Test2021(unittest.TestCase):
    def test_day1(self):
        measures = data_f.read_as_int(1)
        self.assertEqual(day1.count_increment(measures), 1477)
        self.assertEqual(day1.count_increment(measures, 3), 1523)

    def test_day2(self):
        movements = data_f.read_as_list(2)
        self.assertEqual(day2.part1(movements), 1936494)
        self.assertEqual(day2.part2(movements), 1997106066)

    def test_day3(self):
        diagnostics = data_f.read_as_str(3)
        report = list(
            map(lambda x: list(map(int, list(x.rstrip()))), diagnostics))
        self.assertEqual(day3.part1(report), 2261546)
        self.assertEqual(day3.part2(report), 6775520)

    def test_day4(self):
        draw, boards = data_f.read_as_line_matrices(4)
        self.assertEqual(day4.part1(draw, boards), 74320)
        self.assertEqual(day4.part2(draw, boards), 17884)

    def test_day5(self):
        vents = data_f.read_as_list(5)
        vents = [[conv_f.convert_entry_to_point(
            vent[0]), conv_f.convert_entry_to_point(vent[2])] for vent in vents]
        self.assertEqual(day5.part1(vents), 6461)
        self.assertEqual(day5.part2(vents), 18065)


if __name__ == '__main__':
    unittest.main()
