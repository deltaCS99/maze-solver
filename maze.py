from time import sleep
from cell import Cell
class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                x1 = self._x1 + i * self._cell_size_x
                y1 = self._y1 + j * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
        
                cell = Cell(x1, y1, x2, y2, self._win)
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

    def _animate(self):
        self._win.redraw()
        sleep(0.05)