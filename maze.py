from cell import *
import time

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None
    ):
        self.maze_x = x1
        self.maze_y  = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.size_x = cell_size_x
        self.size_y = cell_size_y
        self.win = win
        self._cells = []

        self._create_cells()

    def _create_cells(self):
 
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self._cells.append(col_cells)
        
        maze_width = self.num_cols * self.size_x
        maze_height = self.num_rows * self.size_y

        if maze_width > (self.win._width - self.maze_x):
            raise Exception("maze too wide for window")
        
        if maze_height > (self.win._height - self.maze_y):
            raise Exception("maze too tall for window")
        
        for k in range(0,self.num_cols):
            for l in range(0,self.num_rows):
                print(f"Drawing cell {k},{l}")
                self._draw_cell(k,l)
    
    def _draw_cell(self,i,j):
        cell_x1 = int(abs((self.size_x * i) + self.maze_x))
        cell_y1 = int(abs((self.size_y * j) + self.maze_y))
        cell_x2 = int(abs((self.size_x * (i + 1)) + self.maze_x))
        cell_y2 = int(abs((self.size_y * (j + 1)) + self.maze_y))

        print(f"Drawing cell at: ({i}, {j}) -> ({cell_x1}, {cell_y1}), ({cell_x2}, {cell_y2})")

        self._cells[i][j].draw(cell_x1,cell_y1,cell_x2,cell_y2)

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)

        self._cells[self.num_cols][self.num_rows].has_bottom_wall = False
        self._draw_cell(self.num_cols,self.num_rows)