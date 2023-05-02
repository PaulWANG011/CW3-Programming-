import pprint
# puzzle = [
#     [1, 0, 5, 0, 4, 0, 0, 3, 0],
#     [0, 6, 0, 8, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 2, 0, 0, 0, 0, 8, 0, 0],
#     [0, 0, 0, 0, 3, 1, 0, 0, 0],
#     [0, 7, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 2, 0, 0, 6, 0, 9],
#     [3, 0, 0, 0, 0, 5, 0, 0, 0],
#     [0, 0, 4, 0, 0, 0, 0, 0, 0]
# ]
puzzle=[[0, 2, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 6, 0, 4, 0, 0, 0, 0],
[5, 8, 0, 0, 9, 0, 0, 0, 3],
[0, 0, 0, 0, 0, 3, 0, 0, 4],
[4, 1, 0, 0, 8, 0, 6, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 9, 5],
[2, 0, 0, 0, 1, 0, 0, 8, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 3, 1, 0, 0, 8, 0, 5, 7]]

class SudokuSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.solution = None
        self.domains = [[set(range(1, 10)) if puzzle[a][s] == 0 else set([puzzle[a][s]]) for s in range(9)] for a in range(9)]
        self.initialize_domains()

    def initialize_domains(self):
        for a in range(9):
            for s in range(9):
                if self.puzzle[a][s] != 0:
                    self.eliminate_from_domain(a, s, self.puzzle[a][s])

    def eliminate_from_domain(self, row, col, value):
        if value in self.domains[row][col]:
            self.domains[row][col].remove(value)
            if len(self.domains[row][col]) == 1:
                self.propagate(row, col)

    def propagate(self, row, col):
        value = next(iter(self.domains[row][col]))
        self.puzzle[row][col] = value
        self.eliminate_from_row(row, value)
        self.eliminate_from_column(col, value)
        self.eliminate_from_box(row // 3, col // 3, value)

    def eliminate_from_row(self, row, value):
        for s in range(9):
            self.eliminate_from_domain(row, s, value)

    def eliminate_from_column(self, col, value):
        for a in range(9):
            self.eliminate_from_domain(a, col, value)

    def eliminate_from_box(self, box_row, box_col, value):
        for a in range(box_row * 3, box_row * 3 + 3):
            for s in range(box_col * 3, box_col * 3 + 3):
                self.eliminate_from_domain(a, s, value)

    def is_solved(self):
        return all(self.puzzle[a][s] != 0 for a in range(9) for s in range(9))

    def find_most_constrained_cell(self):
        min_domain_size = 10
        min_cell = None
        for a in range(9):
            for s in range(9):
                if self.puzzle[a][s] == 0 and len(self.domains[a][s]) < min_domain_size:
                    min_domain_size = len(self.domains[a][s])
                    min_cell = (a, s)
        return min_cell

    def solve(self):
        if self.is_solved():
            self.solution = self.puzzle
        else:
            row, col = self.find_most_constrained_cell()
            for value in self.domains[row][col]:
                backup = (self.puzzle, self.domains)
                self.puzzle[row][col] = value
                self.eliminate_from_row(row, value)
                self.eliminate_from_column(col, value)
                self.eliminate_from_box(row // 3, col // 3, value)
                self.solve()
                if self.solution is not None:
                    return
                self.puzzle, self.domains = backup
                
solver = SudokuSolver(puzzle)
solver.solve()
solution = solver.solution
pprint.pprint(solution)