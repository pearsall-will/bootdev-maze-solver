from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=2
        )

class Window:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = 'BootDev - Maze Solver'
        self.__root.protocol('WM_DELETE_WINDOW', self.close)
        self.__canvas = Canvas()
        self.__canvas.pack()
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def draw(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.running = False


class Cell:

    def __init__(self,
        top_left: Point,
        width: int,
        canvas: Canvas,
        left_wall: bool=True,
        right_wall: bool=True,
        bottom_wall: bool=True,
        top_wall: bool=True
    ):
        self.canvas = canvas
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.bottom_wall = bottom_wall
        self.top_wall = top_wall
        self.top_left = top_left
        self.bottom_right = Point(top_left.x+width, top_left.y+width)
        self.top_right = Point(bottom_right.x, top_left.y)
        self.bottom_left =  Point(top_left.x, bottom_right.y)
        self.make_walls()

    def make_walls(self):
        self.walls = []
        if self.right_wall:
            self.walls.append(
                Line(self.top_right, self.bottom_right)
            )
        if self.top_wall:
            self.walls.append(
                Line(self.top_left, self.top_right)
            )
        if self.left_wall:
            self.walls.append(
                Line(self.top_left, self.bottom_left)
            )
        if self.bottom_wall:
            self.walls.append(
                Line(self.bottom_left, self.bottom_right)
            )

    def draw(self, canvas: Canvas):
        for wall in self.walls:
            wall.draw(self.canvas, 'black')
