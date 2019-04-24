from tkinter import *

class Toolbar:
  def __init__(
    self,
    master,
    root,
    on_add_new_node,
    on_remove_node
  ):
    vcmd = master.register(self.validate_num)

    # New node
    Label(root, text="Add node").grid(row=0)
    new_node_entry = Entry(root, validate='all', validatecommand=(vcmd, '%P'))
    new_node_entry.grid(row=1)
    new_node_btn = Button(
      root,
      text="Add",
      command=self.on_entry_submit(new_node_entry, on_add_new_node) 
    )
    new_node_btn.grid(row=2)

    # Remove node 
    Label(root, text="Remove node").grid(row=3)
    remove_node_entry = Entry(root, validate='all', validatecommand=(vcmd, '%P'))
    remove_node_entry.grid(row=4)
    remove_node_btn = Button(
      root,
      text="Remove",
      command=self.on_entry_submit(remove_node_entry, on_remove_node)
    )
    remove_node_btn.grid(row=5)

  def validate_num(self, P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False
  
  def on_entry_submit(self, entry, callback):
    def handle():
      entry_value = entry.get()
      if entry_value:
        callback(int(entry_value))
      
    return handle
