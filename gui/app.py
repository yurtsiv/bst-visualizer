from tkinter import *
from gui.toolbar import Toolbar
from gui.bst_canvas import BSTCanvas
from gui.text_output import TextOutput
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

    # Canvas
    canvas_cont = Frame(master)
    self.bst_canvas = BSTCanvas(master, canvas_cont)
    canvas_cont.grid(row=0, sticky="WENS")
    master.grid_rowconfigure(0)

    # Toolbar & text ouput
    bottom_section = Frame(master)
    bottom_section.grid_columnconfigure(0, minsize=win_width // 2)
    bottom_section.grid_columnconfigure(1, minsize=win_width // 2)
    bottom_section.grid(row=1)

    # Toolbar
    toolbar_cont = Frame(bottom_section)
    self.toolbar = Toolbar(
      master,
      toolbar_cont,
      on_add_new_node=self.on_add_new_node,
      on_remove_node=self.on_remove_node,
      on_show_subtree=self.on_show_subtree,
      on_get_id=self.on_get_id
    )
    toolbar_cont.grid(row=0, column=0, sticky="WENS")

    # Text output
    text_output_cont = Frame(bottom_section)
    text_output_cont.grid(row=0, column=1, sticky="WENS")
    master.update()
    self.text_output = TextOutput(text_output_cont)

  def on_show_subtree(self, root_key):
    self.bst = self.bst.subtree(root_key)
    self.bst_canvas.draw(self.bst)

  def on_add_new_node(self, key):
    self.bst.add(key)
    self.bst_canvas.draw(self.bst)

  def on_remove_node(self, key):
    self.bst.remove(key)
    self.bst_canvas.draw(self.bst)

  def on_get_id(self, key):
    id = self.bst.find(key)
    if id:
      self.text_output.println('ID of ' + str(key) + ': ' + str(id))