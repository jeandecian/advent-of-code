def create_empty_matrix(width, height):
    return [[0 for x in range(width)] for y in range(height)]


def create_empty_matrices(nb_matrices, width, height):
    return [[[0 for x in range(width)] for y in range(height)] for z in range(nb_matrices)]
