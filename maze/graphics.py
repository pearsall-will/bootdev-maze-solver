from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def midpoint(self, point):
        return Point((self.x + point.x)//2,(self.y+ point.y)//2)


class Line():
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
        self.__canvas = Canvas(width=width, height=height)
        self.__canvas.pack()
        self.background = self.__root.cget("bg")
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def draw_line(self, line: Line, fill_color):
        line.draw(self.__canvas, fill_color)


    def close(self):
        self.running = False
