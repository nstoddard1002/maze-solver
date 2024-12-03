from maze import *
from graphics import *

def main():
    num_rows = 32
    num_cols = 40
    margin = 50
    screen_x = 1920
    screen_y = 1080
    cell_size_x = (screen_x - (2 * margin)) // num_cols
    cell_size_y = (screen_y - (2 * margin)) // num_rows

    win = Window(screen_x,screen_y)
    
    maze = Maze(margin,margin,num_rows,num_cols,cell_size_x,cell_size_y,win)

    maze.solve()

    win.wait_for_close()

main()

