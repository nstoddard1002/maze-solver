from tkinter import Tk, BOTH, Canvas

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

        while self.__running is True:
            self.redraw()
    
    def draw_line(self,new_line,fill_color="black"):
        new_line.draw(self.__canvas,fill_color)
    
    def close(self):
        self.__running = False

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line():
    def __init__(self,point_1,point_2):
        self.p1 = point_1
        self.p2 = point_2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x,self.p1.y,self.p2.x,self.p2.y,fill=fill_color,width=2)