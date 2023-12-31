from point import Point
from line import Line
from window import Window
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    num_cols = 12
    num_rows = 10
    maze = Maze(5, 5, num_rows, num_cols, 50, 50, win = win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()
    maze.solve()

    win.wait_for_close()

if __name__ == "__main__":
    main()
