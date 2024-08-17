from maze.graphics import Line, Window, Point
from time import sleep

class Cell:

    def __init__(self,
        top_left: Point,
        width: int,
        height: int,
        window: Window = None,
        left_wall: bool=True,
        right_wall: bool=True,
        bottom_wall: bool=True,
        top_wall: bool=True
    ):
        self._win = window
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.bottom_wall = bottom_wall
        self.top_wall = top_wall
        self.top_left = top_left
        self.bottom_right = Point(top_left.x+width, top_left.y+height)
        self.top_right = Point(self.bottom_right.x, top_left.y)
        self.bottom_left =  Point(top_left.x, self.bottom_right.y)

    def make_walls(self):
        self.walls = [
            (Line(self.top_right, self.bottom_right),self.right_wall),
            (Line(self.top_left, self.top_right), self.top_wall),
            (Line(self.bottom_left, self.top_left),self.left_wall),
            (Line(self.bottom_left,self.bottom_right),self.bottom_wall)
        ]

    def draw(self):
        self.make_walls()
        for wall_tup in self.walls:
            wall = wall_tup[0]
            if wall_tup[1]:
                color = 'black'
            else:
                color = self._win.background
            self._win.draw_line(wall, fill_color=color)

    def midpoint(self):
        return self.top_left.midpoint(self.bottom_right)

    def draw_move(self, to_cell, undo=False):
        line = Line(self.midpoint(), to_cell.midpoint())
        fcolor = 'red'
        if undo:
            fcolor = 'gray'
        self._win.draw_line(line, fill_color=fcolor)

class Maze:

    def __init__(self,
            x: int,
            y: int,
            rows: int,
            cols: int,
            cell_width: int,
            cell_height: int,
            window: Window=None):
        self._start_point = Point(x, y)
        self._rows = rows
        self._cols = cols
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._win = window
        self._create_cells()

    def _create_cells(self):
        sp = self._start_point
        w = self._cell_width
        h = self._cell_height
        self._cells = [[Cell(Point(sp.x+(x*w),sp.y+(y*h)),w,h,self._win) for x in range(self._rows)] for y in range(self._cols)]
        if self._win:
            for column in self._cells:
                for cell in column:
                    self._draw_cell(cell)
        self._animate()

    def _draw_cell(self, cell):
        if self._win:
            cell.draw()

    def _open_maze(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(self._cells[0][0])
        self._cells[-1][-1].bottom_wall = False
        self._draw_cell(self._cells[-1][-1])
        self._animate()

    def _animate(self):
        if self._win is not None:
            self._win.redraw()
            sleep(0.05)
