from maze.graphics import Window
from maze.objects import Maze
import random

if __name__=='__main__':
    width = 1200
    hight = 800
    window = Window(width,hight)
    cell_size = 20
    seed = random.randint(0, 9999999999999999)
    # seed = 9496619031046641
    print(seed)
    maze = Maze(10,10,(hight-20)//cell_size,(width-20)//cell_size,cell_size,cell_size,window, seed=seed)
    maze._open_maze()
    maze._make_maze(0,0)
    maze.solve()
    print(maze.__dict__)
    window.wait_for_close()