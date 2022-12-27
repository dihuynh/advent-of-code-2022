class Solver:
    def __init__(self, input_lines):
        self.rows = self.__parse_rows(input_lines)
        self.columns = self.__parse_columns()
        self.part1 = None
        self.part2 = None

    def __parse_rows(self, lines):
        rows: list[list[int]] = []
        for line in lines:
            rows.append([int(character) for character in list(line)])
        return rows

    def __parse_columns(self):
        columns: list[list[int]] = [[] for _ in range(len(self.rows[0]))]
        for row in self.rows:
            for index, value in enumerate(row):
                columns[index].append(value)
        return columns

    def solve(self):
        visible_from_edges = 4 + (len(self.rows) - 2) * 4
        visible_from_inside: list[tuple] = []
        scenic_scores: list[int] = []
        for i in range(1, len(self.rows) - 1):
            for j in range(1, len(self.rows) - 1):
                current_tree = self.rows[i][j]
                left_trees = self.rows[i][0:j]
                right_trees = self.rows[i][j + 1:]
                top_trees = self.columns[j][0:i]
                bottom_trees = self.columns[j][i + 1:]
                if current_tree > max(left_trees) or current_tree > max(right_trees) \
                        or current_tree > max(top_trees) or current_tree > max(bottom_trees):
                    visible_from_inside.append((i, j))

                top_score = self.__find_score(top_trees[::-1], current_tree)
                left_score = self.__find_score(left_trees[::-1], current_tree)
                right_score = self.__find_score(right_trees, current_tree)
                bottom_score = self.__find_score(bottom_trees, current_tree)

                # print(f'for ({i}, {j}) top: {top_score}, left: {left_score}, right: {right_score}, bottom: {bottom_score}')

                scenic_scores.append(top_score*left_score*right_score*bottom_score)

        self.part1 = len(visible_from_inside) + visible_from_edges
        self.part2 = max(scenic_scores)

    def __find_score(self, trees, current_tree):
        score = 0
        for tree in trees:
            if tree < current_tree:
                score += 1
            elif tree >= current_tree:
                score += 1
                break
        return score



