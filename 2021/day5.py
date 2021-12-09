import calculator_functions as calc_f
import converter_functions as conv_f
import create_functions as crea_f
import data_functions as data_f
import display_functions as disp_f
import find_functions as find_f


def part1(vents):
    max_y, max_x = find_f.find_max_vents(vents)
    diagram = crea_f.create_empty_matrix(max_x+1, max_y+1)

    for vent in vents:
        if (vent[0][0] == vent[1][0]):
            vertical_line_min, vertical_line_max = find_f.find_vertical_line_min_max(
                vent)
            x = vent[0][0]
            for y in range(vertical_line_min, vertical_line_max+1):
                diagram[y][x] += 1

        elif (vent[0][1] == vent[1][1]):
            horizontal_line_min, horizontal_line_max = find_f.find_horizontal_line_min_max(
                vent)
            y = vent[0][1]
            for x in range(horizontal_line_min, horizontal_line_max+1):
                diagram[y][x] += 1

    return calc_f.calculate_lines_overlap(diagram)


def part2(vents):
    max_y, max_x = find_f.find_max_vents(vents)
    diagram = crea_f.create_empty_matrix(max_x+1, max_y+1)

    for vent in vents:
        if (vent[0][0] == vent[1][0]):
            vertical_line_min, vertical_line_max = find_f.find_vertical_line_min_max(
                vent)
            x = vent[0][0]
            for y in range(vertical_line_min, vertical_line_max+1):
                diagram[y][x] += 1

        elif (vent[0][1] == vent[1][1]):
            horizontal_line_min, horizontal_line_max = find_f.find_horizontal_line_min_max(
                vent)
            y = vent[0][1]
            for x in range(horizontal_line_min, horizontal_line_max+1):
                diagram[y][x] += 1

        else:
            start, end = min(vent), max(vent)
            delta_x, delta_y = end[0]-start[0], end[1]-start[1]
            x, y = start[0], start[1]

            for i in range(delta_x+1):
                diagram[y][x] += 1
                y += int(1 * delta_y/abs(delta_y))
                x += int(1 * delta_x/abs(delta_x))

    return calc_f.calculate_lines_overlap(diagram)


if __name__ == '__main__':
    vents = data_f.read_as_list(5)
    vents = [[conv_f.convert_entry_to_point(
        vent[0]), conv_f.convert_entry_to_point(vent[2])] for vent in vents]
    disp_f.display_part(1, part1(vents))
    disp_f.display_part(2, part2(vents))
