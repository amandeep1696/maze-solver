from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()

        self.root.title("Maze Solver")

        self.canvas = Canvas(self.root, width=width, height=height)

        self.canvas.pack(fill=BOTH, expand=True)
        
        self.is_running = False