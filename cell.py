from tkinter import LEFT, TOP, RIGHT, BOTTOM
from point import Point
from line import Line

class Cell:
    def __init__(self, x1, y1, x2, y2, visited = False, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = visited

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self._win = win

    def draw(self):
        fill_color = "black"
        top_left = Point(self._x1, self._y1)
        bottom_right = Point(self._x2, self._y2)

        left_wall = Line(Point(top_left.x, top_left.y), Point(top_left.x, bottom_right.y))
        right_wall = Line(Point(bottom_right.x, top_left.y), Point(bottom_right.x, bottom_right.y))
        top_wall = Line(Point(top_left.x, top_left.y), Point(bottom_right.x, top_left.y))
        bottom_wall = Line(Point(top_left.x, bottom_right.y), Point(bottom_right.x, bottom_right.y))

        if self.has_left_wall:
            self._win.draw_line(left_wall, fill_color)
        if self.has_right_wall:
            self._win.draw_line(right_wall, fill_color)
        if self.has_top_wall:
            self._win.draw_line(top_wall, fill_color)
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall, fill_color)
        if not self.has_left_wall:
            self._win.draw_line(left_wall, "#d9d9d9")
        if not self.has_right_wall:
            self._win.draw_line(right_wall, "#d9d9d9")
        if not self.has_top_wall:
            self._win.draw_line(top_wall, "#d9d9d9")
        if not self.has_bottom_wall:
            self._win.draw_line(bottom_wall, "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        from_x = (self._x1 + self._x2) // 2
        from_y = (self._y1 + self._y2) // 2

        to_x = (to_cell._x1 + to_cell._x2) // 2
        to_y = (to_cell._y1 + to_cell._y2) // 2

        line = Line(Point(from_x, from_y), Point(to_x, to_y))

        line_color = "green" if undo else "red"
        self._win.draw_line(line, line_color)
    
    def has_wall_to(self, dir_i, dir_j):
        if dir_i == -1:
            return self.has_left_wall
        elif dir_i == 1:
            return self.has_right_wall
        elif dir_j == -1:
            return self.has_top_wall
        elif dir_j == 1:
            return self.has_bottom_wall
