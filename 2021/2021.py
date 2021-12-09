import unittest
import data_functions as data_f
import day1
import day2


class Test2021(unittest.TestCase):
    def test_day1(self):
        measures = data_f.read_as_int(1)
        self.assertEqual(day1.count_increment(measures), 1477)
        self.assertEqual(day1.count_increment(measures, 3), 1523)

    def test_day2(self):
        movements = data_f.read_as_list(2)
        self.assertEqual(day2.part1(movements), 1936494)
        self.assertEqual(day2.part2(movements), 1997106066)


if __name__ == '__main__':
    unittest.main()
