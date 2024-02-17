from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()
            self.root.after(100)  
    
    def close(self):
        self.is_running = False
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x  
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y,
            fill=fill_color, width=2
        )
        canvas.pack(fill="both", expand=True)

if __name__ == "__main__":
    window = Window(800, 600)
    point1 = Point(100, 150)
    point2 = Point(700, 450)
    line = Line(point1, point2)
    
    window.draw_line(line, "blue")
    
    window.wait_for_close()
    

