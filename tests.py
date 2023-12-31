import unittest
from maze import Maze
from window import Window

win = Window(800, 600)

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(5, 5, num_rows, num_cols, 50, 50, win = win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_reset_cells_visited(self):
            num_cols = 12
            num_rows = 10
            m1 = Maze(5, 5, num_rows, num_cols, 50, 50, win = win)

            # Set some cells as visited
            m1._cells[1][1].visited = True
            m1._cells[2][2].visited = True
            m1._cells[3][3].visited = True

            # Call reset_cells_visited
            m1._reset_cells_visited()

            # Check if all cells have visited set back to False
            for i in range(num_cols):
                for j in range(num_rows):
                    self.assertFalse(m1._cells[i][j].visited)

if __name__ == "__main__":
    unittest.main()

