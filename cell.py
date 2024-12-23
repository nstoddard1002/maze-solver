from graphics import *


class Cell():
    def __init__(self,window=None):
        self.has_left_wall=True
        self.has_right_wall=True
        self.has_top_wall=True
        self.has_bottom_wall=True
        
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None

        self._win = window

        self.visited = False

    def draw(self,x1,y1,x2,y2):
        if self._win is None:
            return

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        #debug print statement
        #print(f"drawing cell with points {x1},{y1} and {x2},{y2}")

        if self.has_left_wall:
            line = Line(Point(x1,y1), Point(x1,y2))
            #print(f"Drawing cell walls at: ({x1}, {y1}) -> ({x1}, {y2}) with color: black")
            self._win.draw_line(line,"black")
        if self.has_bottom_wall:
            line = Line(Point(x1,y2), Point(x2,y2))
            #print(f"Drawing cell walls at: ({x1}, {y2}) -> ({x2}, {y2}) with color: black")
            self._win.draw_line(line,"black")
        if self.has_right_wall:
            line = Line(Point(x2,y2), Point(x2,y1))
            #print(f"Drawing cell walls at: ({x2}, {y2}) -> ({x2}, {y1}) with color: black")
            self._win.draw_line(line,"black")
        if self.has_top_wall:
            line = Line(Point(x2,y1), Point(x1,y1))
            #print(f"Drawing cell walls at: ({x2}, {y1}) -> ({x2}, {y2}) with color: black")
            self._win.draw_line(line,"black")
        
        if self.has_left_wall is False:
            line = Line(Point(x1,y1), Point(x2,y2))
            #print(f"Drawing cell walls at: ({x1}, {y1}) -> ({x1}, {y2}) with color: white")
            self._win.draw_line(line,"white")
        if self.has_bottom_wall is False:
            line = Line(Point(x1,y2), Point(x2,y2))
            #print(f"Drawing cell walls at: ({x1}, {y2}) -> ({x2}, {y2}) with color: white")
            self._win.draw_line(line,"white")
        if self.has_right_wall is False:
            line = Line(Point(x2,y2), Point(x2,y1))
            #print(f"Drawing cell walls at: ({x2}, {y2}) -> ({x2}, {y1}) with color: white")
            self._win.draw_line(line,"white")
        if self.has_top_wall is False:
            line = Line(Point(x2,y1), Point(x1,y1))
            #print(f"Drawing cell walls at: ({x2}, {y1}) -> ({x1}, {y1}) with color: white")
            self._win.draw_line(line,"white")
    
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