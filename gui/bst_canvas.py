from tkinter import *


class BSTCanvas:
  def __init__(self, master, root):
    self.canvas = Canvas(root, width=master.winfo_screenwidth() // 1.5)
    self.canvas.pack()

  def draw(self, bst):
    self.canvas.delete('all')
    bst.draw(self.canvas)