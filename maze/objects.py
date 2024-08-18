from maze.graphics import Line, Window, Point
from time import sleep
import random
from math import inf


class Vector:

    def __init__(self, x: int, y: int, max_x: int=inf, max_y: int=inf):
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y

    def __add__(self, vector):
        return Vector(
            max(min(self.x + vector.x, self.max_x),0),
            max(min(self.y + vector.y, self.max_y),0),
            max_x=self.max_x,
            max_y=self.max_y
            )
    def __eq__(self, vector):
        return (self.x==vector.x and self.y==vector.y)

    def __repr__(self):
        return f'x:{self.x}, y:{self.y}, max_x:{self.max_x}, max_y:{self.max_y}'

LEFT = Vector(-1,0)
RIGHT = Vector(1,0)
UP = Vector(0,-1)
DOWN = Vector(0,1)

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
        self.visited = False

    def get_paths(self):
        paths = []
        if not self.bottom_wall:
            paths.append(DOWN)
        if not self.right_wall:
            paths.append(RIGHT)
        if not self.left_wall:
            paths.append(LEFT)
        if not self.top_wall:
            paths.append(UP)
        return paths

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
            window: Window=None,
            seed: int= None):
        if seed:
            random.seed(seed)
        else:
            random.seed(0)
        self._start_point = Point(x, y)
        self._rows = rows
        self._cols = cols
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._win = window
        self._create_cells()

    def solve(self):
        self._solve_recursive(Vector(0,0,self._cols-1,self._rows-1))

    def _solve_recursive(self, vec):
        self._animate()
        cell = self._cells[vec.x][vec.y]
        cell.visited = True
        if vec.x == vec.max_x and vec.y == vec.max_y:
            return True
        for path in cell.get_paths():
            new_vec = vec + path
            nex_cell = self._cells[new_vec.x][new_vec.y]
            if not nex_cell.visited:
                cell.draw_move(self._cells[new_vec.x][new_vec.y])
                done = self._solve_recursive(new_vec)
                if done:
                    return True
                cell.draw_move(self._cells[new_vec.x][new_vec.y], True)
        return False

    def _make_maze(self, x: int,y: int, visited: list=[]):
        vec = Vector(x,y, self._cols-1, self._rows-1)
        while True:
            visited.append(vec)
            choices = [point for point in [LEFT,RIGHT,UP,DOWN] if vec + point not in visited]
            if not choices:
                visited.append(vec)
                return
            next_dir = random.choice(choices)
            next_vec = vec + next_dir
            if next_dir == LEFT:
                self._cells[vec.x][vec.y].left_wall = False
                self._cells[next_vec.x][next_vec.y].right_wall = False
            elif next_dir == RIGHT:
                    self._cells[vec.x][vec.y].right_wall = False
                    self._cells[next_vec.x][next_vec.y].left_wall = False
            elif next_dir == UP:
                    self._cells[vec.x][vec.y].top_wall = False
                    self._cells[next_vec.x][next_vec.y].bottom_wall = False
            elif next_dir == DOWN:
                    self._cells[vec.x][vec.y].bottom_wall = False
                    self._cells[next_vec.x][next_vec.y].top_wall = False
            self._draw_cell(self._cells[next_vec.x][next_vec.y])
            self._draw_cell(self._cells[vec.x][vec.y])
            self._make_maze(next_vec.x, next_vec.y, visited)

    def _reset_cells(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _create_cells(self):
        sp = self._start_point
        w = self._cell_width
        h = self._cell_height
        self._cells = [[Cell(Point(sp.x+(x*w),sp.y+(y*h)),w,h,self._win) for y in range(self._rows)] for x in range(self._cols)]
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
            sleep(0.025)
