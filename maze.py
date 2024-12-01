from tkinter import Tk, BOTH, Canvas
import time


class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")

        self._width = width
        self._height = height

        #these were using grid
        #self.root.columnconfigure(0,weight=1)
        #self.root.rowconfigure(0,weight=1)

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, bg="white", height=height,width=width)
        
        self.__canvas.pack(fill=BOTH,expand=1)
        #self.canvas.grid(column=0,row=0,sticky=(N,W,E,S))

        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True

        while self.is_running is True:
            self.redraw()
    
    def draw_line(self,new_line,fill_color):
        new_line.draw(self.__canvas,fill_color)
    
    def close(self):
        self.__running = False

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line():
    def __init__(self,point_1,point_2):
        self.p1 = point_2
        self.p2 = point_2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x,self.p1.y,self.p2.x,self.p2.y,fill=fill_color,width=2)

class Cell():
    def __init__(self,window):
        self.has_left_wall=True
        self.has_right_wall=True
        self.has_top_wall=True
        self.has_bottom_wall=True
        
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None

        self._win = window

    def draw(self,x1,y1,x2,y2):
        if self._win is None:
            return

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        if self.has_left_wall:
            line = Line(Point(x1,y1), Point(x2,y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1,y2), Point(x2,y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2,y2), Point(x2,y1))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x2,y1), Point(x1,y1))
            self._win.draw_line(line)
    
    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        
        start_x = abs(self._x1 + self._x2) // 2
        start_y = abs(self._y1 + self._y2) // 2

        end_x = abs(to_cell._x1 + to_cell._x2) // 2
        end_y = abs(to_cell._y1 + to_cell._y2) // 2

        line = Line(Point(start_x,start_y),Point(end_x,end_y))
        self._win.draw_line(line,color)

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win
    ):
        self.maze_x = x1
        self.maze_y  = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.size_x = cell_size_x
        self.size_y = cell_size_y
        self.win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_rows):
            row_cells = []
            for j in range(self.num_cols):
                row_cells.append(Cell(self.win))
            self._cells.append(row_cells)
        
        maze_width = num_cols * self.size_x
        maze_height = num_rows * self.size_y

        if maze_width > (self.win._width - self.maze_x):
            raise Exception("maze too wide for window")
        
        if maze_height > (self.win._height - self.maze_y):
            raise Exception("maze too tall for window")
        
        for k in range(0,self.num_rows):
            for l in range(0,self.num_cols):
                self._draw_cell(k,l)
    
    def _draw_cell(self,i,j):
        cell_x1 = self.size_x * i 
        cell_y1 = self.size_y * j
        cell_x2 = self.size_x * (i + 1)
        cell_y2 = self.size_y * (j + 1)

        cell_x1 += self.maze_x
        cell_y1 += self.maze_y
        cell_x2 += self.maze_x
        cell_y2 += self.maze_y

        self._cells[i][j].draw(cell_x1,cell_y1,cell_x2,cell_y2)

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
        
        

        
        

