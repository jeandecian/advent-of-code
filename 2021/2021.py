import unittest
import data_functions as data_f
import day1


class Test2021(unittest.TestCase):
    def test_day1(self):
        measures = data_f.read_as_int(1)
        self.assertEqual(day1.count_increment(measures), 1477)
        self.assertEqual(day1.count_increment(measures, 3), 1523)


if __name__ == '__main__':
    unittest.main()
