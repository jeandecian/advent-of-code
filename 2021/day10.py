import utils


def part1(navigation_subsystem):
    opening_chunk = ('(', '[', '{', '<')
    closing_chunk = (')', ']', '}', '>')
    closing_chunk_score = (3, 57, 1197, 25137)

    syntax_error_score = 0

    for line in navigation_subsystem:
        chunk = []
        for side_chunk in line:
            if (side_chunk in opening_chunk):
                chunk.append(side_chunk)
            elif (side_chunk in closing_chunk and opening_chunk.index(chunk[-1]) == closing_chunk.index(side_chunk)):
                chunk.pop(-1)
            else:
                syntax_error_score += closing_chunk_score[closing_chunk.index(
                    side_chunk)]
                break

    return syntax_error_score


def part2(navigation_subsystem):
    opening_chunk = ('(', '[', '{', '<')
    closing_chunk = (')', ']', '}', '>')

    autocomplete_scores = []

    for line in navigation_subsystem:
        chunk = []
        incomplete = True
        for side_chunk in line:
            if (side_chunk in opening_chunk):
                chunk.append(side_chunk)
            elif (side_chunk in closing_chunk and opening_chunk.index(chunk[-1]) == closing_chunk.index(side_chunk)):
                chunk.pop(-1)
            else:
                incomplete = False
                break

        if (incomplete):
            chunk.reverse()
            score = 0

            for side_chunk in chunk:
                score *= 5
                score += opening_chunk.index(side_chunk) + 1

            autocomplete_scores.append(score)

    return sorted(autocomplete_scores)[len(autocomplete_scores)//2]


if __name__ == '__main__':
    navigation_subsystem = utils.read_as_str(10)
    navigation_subsystem = [list(line.rstrip())
                            for line in navigation_subsystem]
    utils.display_part(1, part1(navigation_subsystem))
    utils.display_part(2, part2(navigation_subsystem))
