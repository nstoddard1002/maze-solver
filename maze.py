from cell import *
import time
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        seed=None
    ):
        self.maze_x = x1
        self.maze_y  = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.size_x = cell_size_x
        self.size_y = cell_size_y
        self.win = win
        self._cells = []
        if seed is None:
            self.seed = random.seed()
        else:
            self.seed = random.seed(seed)

        self._create_cells()
        
        self._break_entrance_and_exit()

        self._break_walls_r(self.num_cols-1,self.num_rows-1)

        self._reset_cells_visited()

    def _create_cells(self):
 
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self._cells.append(col_cells)
        
        maze_width = self.num_cols * self.size_x
        maze_height = self.num_rows * self.size_y

        if maze_width > (self.win._width - (2*self.maze_x)):
            raise Exception("maze too wide for window")
        
        if maze_height > (self.win._height - (2*self.maze_y)):
            raise Exception("maze too tall for window")
        
        for k in range(0,self.num_cols):
            for l in range(0,self.num_rows):
                #print(f"Drawing cell {k},{l}")
                self._draw_cell(k,l)
    
    def _draw_cell(self,i,j):
        cell_x1 = int(abs((self.size_x * i) + self.maze_x))
        cell_y1 = int(abs((self.size_y * j) + self.maze_y))
        cell_x2 = int(abs((self.size_x * (i + 1)) + self.maze_x))
        cell_y2 = int(abs((self.size_y * (j + 1)) + self.maze_y))

        #print(f"Drawing cell at: ({i}, {j}) -> ({cell_x1}, {cell_y1}), ({cell_x2}, {cell_y2})")

        self._cells[i][j].draw(cell_x1,cell_y1,cell_x2,cell_y2)

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)

        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1,self.num_rows-1)

    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            stuck = True
            #checks if next cell to the right exists and has been visited
            if i+1 < len(self._cells):
                if self._cells[i+1][j].visited == False:
                    to_visit.append(((i+1),j))
                    stuck = False
            #checks if next cell down exists and has been visited
            if j+1 < len(self._cells[i]):
                if self._cells[i][j+1].visited == False:
                    to_visit.append((i,(j+1)))
                    stuck = False
            #checks if next cell to the left exists and has been visited
            if i-1 >= 0:
                if self._cells[i-1][j].visited == False:
                    to_visit.append(((i-1),j))
                    stuck = False
            #checks if next cell up exists and has been visited
            if j-1 >= 0:
                if self._cells[i][j-1].visited == False:
                    to_visit.append((i,(j-1)))
                    stuck = False
            if stuck is True:
                self._draw_cell(i,j)
                return
            next_direction = to_visit[random.randint(0,(len(to_visit)-1))]

            next_direction_x = next_direction[0]
            next_direction_y = next_direction[1]

            if next_direction_x == i and next_direction_y > j:
                self._cells[i][j+1].has_top_wall = False
                self._cells[i][j].has_bottom_wall = False
                self._draw_cell(i,j+1)
                self._draw_cell(i,j)
                self._break_walls_r(i,j+1)
            elif next_direction_x == i and next_direction_y < j:
                self._cells[i][j-1].has_bottom_wall = False
                self._cells[i][j].has_top_wall = False
                self._draw_cell(i,j-1)
                self._draw_cell(i,j)
                self._break_walls_r(i,j-1)
            elif next_direction_x > i and next_direction_y == j:
                self._cells[i+1][j].has_left_wall = False
                self._cells[i][j].has_right_wall = False
                self._draw_cell(i+1,j)
                self._draw_cell(i,j)
                self._break_walls_r(i+1,j)
            elif next_direction_x < i and next_direction_y == j:
                self._cells[i-1][j].has_right_wall = False
                self._cells[i][j].has_left_wall = False
                self._draw_cell(i-1,j)
                self._draw_cell(i,j)
                self._break_walls_r(i-1,j)

    def _reset_cells_visited(self):
        for column in self._cells:
            for row in column:
                row.visited = False
    
    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self,i,j):
        self._animate()
        
        self._cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        if i + 1 < len(self._cells):
            if self._cells[i+1][j].visited is False:
                if self._cells[i][j].has_right_wall is False:
                    self._cells[i][j].draw_move(self._cells[i+1][j])
                    if self._solve_r(i+1,j) is True:
                        return True
                    self._cells[i][j].draw_move(self._cells[i+1][j],True)

        if i - 1 >= 0:
            if self._cells[i-1][j].visited is False:
                if self._cells[i][j].has_left_wall is False:
                    self._cells[i][j].draw_move(self._cells[i-1][j])
                    if self._solve_r(i-1,j) is True:
                        return True
                    self._cells[i][j].draw_move(self._cells[i-1][j],True)
        
        if j + 1 < len(self._cells[i]):
            if self._cells[i][j+1].visited is False:
                if self._cells[i][j].has_bottom_wall is False:
                    self._cells[i][j].draw_move(self._cells[i][j+1])
                    if self._solve_r(i,j+1) is True:
                        return True
                    self._cells[i][j].draw_move(self._cells[i][j+1],True)

        if j - 1 >= 0:
            if self._cells[i][j-1].visited is False:
                if self._cells[i][j].has_top_wall is False:
                    self._cells[i][j].draw_move(self._cells[i][j-1])
                    if self._solve_r(i,j-1) is True:
                        return True
                    self._cells[i][j].draw_move(self._cells[i][j-1],True)
        
        return False
