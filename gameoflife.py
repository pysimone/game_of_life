# Just another Conway's Game of Life
# with glider spaceship example
# entirely written in Python 3

ROWS = 10
COLUMNS = 10


def empty_grid(rows=ROWS, columns=COLUMNS):
    return [[0 for j in range(columns)] for i in range(rows)]


class GameOfLife:

    def __init__(self):
        self.grid = empty_grid()
        self.set_glider()

    def set_glider(self):
        self.grid[3][1] = 1
        self.grid[3][2] = 1
        self.grid[3][3] = 1
        self.grid[2][3] = 1
        self.grid[1][2] = 1

    def neighbours(self, i, j):
        return (self.grid[i - 1][j - 1] +
                self.grid[i][j - 1] +
                self.grid[i + 1][j - 1] +
                self.grid[i - 1][j] +
                self.grid[i + 1][j] +
                self.grid[i - 1][j + 1] +
                self.grid[i][j + 1] +
                self.grid[i + 1][j + 1])

    def next_generation(self):
        g = empty_grid()
        for i in range(1, ROWS - 1):
            for j in range(1, COLUMNS - 1):
                nbs = self.neighbours(i, j)
                cel = self.grid[i][j]
                if cel == 1:
                    if nbs == 2 or nbs == 3:
                        g[i][j] = 1
                    else:
                        g[i][j] = 0
                else:
                    if nbs == 3:
                        g[i][j] = 1
                    else:
                        g[i][j] = 0
        self.grid = g

    def __str__(self):
        s = []
        for i in range(ROWS):
            s.append(
                ' '.join([str(item) for item in self.grid[i]])
            )

        return '\n'.join(s)


gol = GameOfLife()
print("Glider")
print(gol)
for c in range(1, 5):
    print('')
    print("Generation", c)
    gol.next_generation()
    print(gol)
