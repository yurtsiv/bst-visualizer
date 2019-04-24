from tkinter import *
from gui.sidebar import Sidebar
from gui.bst_canvas import BSTCanvas
from bst import BST

class App:
  bst = BST()

  def __init__(self, master):
    master.wm_attributes('-zoomed', True)
    master.update()

    win_width = master.winfo_width()
    win_height = master.winfo_height()

    master.grid_rowconfigure(0, minsize=win_height*0.75)
    master.grid_rowconfigure(1, minsize=win_height*0.25)
    master.grid_columnconfigure(0, minsize=win_width)

    canvas_cont = Frame(master)
    self.bst_canvas = BSTCanvas(master, canvas_cont)
    canvas_cont.grid(row=0, sticky="WENS")
    master.grid_rowconfigure(0)

    sidebar_cont = Frame(master)
    self.sidebar = Sidebar(master, sidebar_cont)
    self.sidebar.on_add_new_node(self.on_add_new_node)
    sidebar_cont.grid(row=1, sticky="WENS")


  def on_add_new_node(self, key):
    self.bst.add(key)
    self.bst_canvas.draw(self.bst)
