import utils


def is_low_point(heightmap, y, x):
    height = len(heightmap)
    width = len(heightmap[0])

    point = heightmap[y][x]

    if (x > 0 and point >= heightmap[y][x-1]):
        return False

    if (x < width-1 and point >= heightmap[y][x+1]):
        return False

    if (y > 0 and point >= heightmap[y-1][x]):
        return False

    if (y < height-1 and point >= heightmap[y+1][x]):
        return False

    return True


def calculate_basin_size(heightmap, y, x, heightmap_mask):
    point = heightmap[y][x]

    if (heightmap[y][x] == 9):
        return 0

    basin_size = 1

    height = len(heightmap)
    width = len(heightmap[0])

    if (x > 0 and point < heightmap[y][x-1] and heightmap_mask[y][x-1] == 0):
        basin_size += calculate_basin_size(heightmap, y, x-1, heightmap_mask)

    if (x < width-1 and point < heightmap[y][x+1] and heightmap_mask[y][x+1] == 0):
        basin_size += calculate_basin_size(heightmap, y, x+1, heightmap_mask)

    if (y > 0 and point < heightmap[y-1][x] and heightmap_mask[y-1][x] == 0):
        basin_size += calculate_basin_size(heightmap, y-1, x, heightmap_mask)

    if (y < height-1 and point < heightmap[y+1][x] and heightmap_mask[y+1][x] == 0):
        basin_size += calculate_basin_size(heightmap, y+1, x, heightmap_mask)

    heightmap_mask[y][x] = 1

    return basin_size


def part1(heightmap):
    risk_level = 0

    height = len(heightmap)
    width = len(heightmap[0])

    for y in range(height):
        for x in range(width):
            if (is_low_point(heightmap, y, x)):
                risk_level += heightmap[y][x] + 1

    return risk_level


def part2(heightmap):
    basins = []

    height = len(heightmap)
    width = len(heightmap[0])

    for y in range(height):
        for x in range(width):
            if (is_low_point(heightmap, y, x)):
                heightmap_mask = utils.create_empty_matrix(width, height)
                basins.append(calculate_basin_size(
                    heightmap, y, x, heightmap_mask))

    largest_basins_size = 1

    for basins_size in sorted(basins, reverse=True)[:3]:
        largest_basins_size *= basins_size

    return largest_basins_size


if __name__ == '__main__':
    heightmap = utils.read_as_str(9)
    heightmap = [list(map(int, list(str(height.rstrip()))))
                 for height in heightmap]
    utils.display_part(1, part1(heightmap))
    utils.display_part(2, part2(heightmap))
