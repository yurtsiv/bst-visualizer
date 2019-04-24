from tkinter import *

class Toolbar:
  def __init__(self, master, root):
    Label(root, text="Add new node").grid(row=0)

    vcmd = master.register(self.validate_num)
    self.new_node_entry = Entry(root, validate='all', validatecommand=(vcmd, '%P'))
    self.new_node_entry.grid(row=1)
  
    self.new_node_btn = Button(root, text="Add", command=self.on_add_new_node_btn_click)
    self.new_node_btn.grid(row=2)
  
  def validate_num(self, P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False
  
  def on_add_new_node(self, callback):
    self._on_add_new_node = callback
  
  def on_add_new_node_btn_click(self):
    entry_value = self.new_node_entry.get()
    if entry_value:
      self._on_add_new_node(int(entry_value))