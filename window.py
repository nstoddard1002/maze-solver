from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")

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
        
        start_x = (self._x1 + self._x2) / 2
        start_y = (self._y1 + self._y2) / 2

        end_x = (to_cell._x1 + to_cell._x2) / 2
        end_y = (to_cell._y1 + to_cell._y2) / 2

        line = Line(Point(start_x,start_y),Point(end_x,end_y))
        self._win.draw_line(line,color)

        
        

