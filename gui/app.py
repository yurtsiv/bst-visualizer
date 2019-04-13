from tkinter import *
from gui import Sidebar

class App:
  def set_sizes(self, node, width, height):
    node.geometry("{0}x{1}".format(width, height))

  def __init__(self, master):
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()

    self.set_sizes(master, screen_width, screen_height)

    sidebar_cont = Frame(master)
    sidebar_cont.grid(column=0)
    self.sidebar = Sidebar(master, sidebar_cont)
    self.sidebar.on_add_new_node(self.on_add_new_node)

    canvas_cont = Frame(master)
    canvas_cont.grid(column=1)
    self.sidebar2 = Sidebar(master, canvas_cont)

  def on_add_new_node(self, key):
    print(key)
