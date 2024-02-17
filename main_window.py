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

class Point:
    def __init__(self, x=0, y=0):
        self.x = x  
        self.y = y

if __name__ == "__main__":
    win = Window(800, 600)
    win.wait_for_close()
    

