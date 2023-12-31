import random
from time import sleep
from cell import Cell
class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, seed = None, win = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._seed = seed

        if self._seed is not None:
            random.seed(self._seed)

        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                x1 = self._x1 + i * self._cell_size_x
                y1 = self._y1 + j * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
        
                cell = Cell(x1, y1, x2, y2, win = self._win)
                self._draw_cell(cell, i, j)
                column.append(cell)
            self._cells.append(column)

    def _draw_cell(self,cell, i, j):
        cell.draw()
        self._animate()
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(self._cells[i][j], i, j)
            
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            directions = []
            if i > 0 and not self._cells[i - 1][j].visited:
                directions.append((-1, 0))
            if i  < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                directions.append((1, 0))
            if j > 0 and not self._cells[i][j - 1].visited:
                directions.append((0, -1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                directions.append((0, 1))

            if not directions:
                self._draw_cell(self._cells[i][j], i, j)
                return
            
            direction = random.choice(directions)
            new_i, new_j = i + direction[0], j + direction[1]

            if direction == (-1, 0):  # Move left
                self._cells[i][j].has_left_wall = False
                self._cells[new_i][new_j].has_right_wall = False
            elif direction == (1, 0):  # Move right
                self._cells[i][j].has_right_wall = False
                self._cells[new_i][new_j].has_left_wall = False
            elif direction == (0, -1):  # Move up
                self._cells[i][j].has_top_wall = False
                self._cells[new_i][new_j].has_bottom_wall = False
            elif direction == (0, 1):  # Move down
                self._cells[i][j].has_bottom_wall = False
                self._cells[new_i][new_j].has_top_wall = False

            self._break_walls_r(new_i, new_j)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
    
    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]# Left, Right, Up, Down

        for direction in directions:
            new_i, new_j = i + direction[0], j + direction[1]
            if (
                0 <= new_i < self._num_cols
                and 0 <= new_j < self._num_rows
                and not self._cells[i][j].has_wall_to(direction[0], direction[1])
                and not self._cells[new_i][new_j].visited
            ):
                
                self._cells[i][j].draw_move(self._cells[new_i][new_j], undo = True)

                if self._solve_r(new_i, new_j):
                    return True
                self._cells[i][j].draw_move(self._cells[new_i][new_j])

        return False

    def _animate(self):
        self._win.redraw()
        sleep(0.05)