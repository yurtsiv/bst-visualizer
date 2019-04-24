from tkinter import *

class BSTCanvas:
  def __init__(self, master, root):
    self.canvas = Canvas(root)
    self.canvas.pack()

  def draw(self, bst):
    self.canvas.delete('all')
    bst.draw(
      self.canvas,
      {
        'x': self.canvas.winfo_width() // 2,
        'y': 20
      }
    )