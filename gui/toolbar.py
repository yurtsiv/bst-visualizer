from tkinter import *

class Toolbar:
  def __init__(
    self,
    master,
    root,
    on_add_new_node,
    on_remove_node,
    on_show_subtree,
    on_get_id,
    on_size_click,
    on_root_click,
    on_min_click,
    on_max_click,
    on_print_click,
    on_clear_click
  ):
    vcmd = master.register(self.validate_num)

    # New node
    Label(root, text="Add node").grid(row=0, column=0)
    new_node_entry = Entry(root, validate='all', validatecommand=(vcmd, '%P'))
    new_node_entry.grid(row=1, column=0)
    new_node_btn = Button(
      root,
      text="Add",
      command=self.on_entry_submit(new_node_entry, on_add_new_node) 
    )
    new_node_btn.grid(row=2, column=0)

    # Remove node 
    Label(root, text="Remove node").grid(row=3, column=0)
    remove_node_entry = Entry(root, validate='all', validatecommand=(vcmd, '%P'))
    remove_node_entry.grid(row=4, column=0)
    remove_node_btn = Button(
      root,
      text="Remove",
      command=self.on_entry_submit(remove_node_entry, on_remove_node)
    )
    remove_node_btn.grid(row=5, column=0)

    # Subtree 
    Label(root, text="Subtree").grid(row=0, column=1)
    show_subtree_entry = Entry(root, validate='all', validatecommand=(vcmd, '%P'))
    show_subtree_entry.grid(row=1, column=1)
    show_subtree_btn = Button(
      root,
      text="Show",
      command=self.on_entry_submit(show_subtree_entry, on_show_subtree)
    )
    show_subtree_btn.grid(row=2, column=1)

    # Get ID 
    Label(root, text="Get ID").grid(row=3, column=1)
    get_id_entry = Entry(root, validate='all', validatecommand=(vcmd, '%P'))
    get_id_entry.grid(row=4, column=1)
    get_id_btn = Button(
      root,
      text="Get",
      command=self.on_entry_submit(get_id_entry, on_get_id)
    )
    get_id_btn.grid(row=5, column=1)

    # Size
    size_btn = Button(root, text="Size", command=on_size_click)
    size_btn.grid(row=1, column=2) 

    # Root
    root_btn = Button(root, text="Root", command=on_root_click)
    root_btn.grid(row=2, column=2) 

    # Min
    min_btn = Button(root, text="Min", command=on_min_click)
    min_btn.grid(row=3, column=2) 

    # Max
    max_btn = Button(root, text="Max", command=on_max_click)
    max_btn.grid(row=1, column=3) 

    # Print
    print_btn = Button(root, text="Print", command=on_print_click)
    print_btn.grid(row=2, column=3) 

    # Clear
    clear_btn = Button(root, text="Clear", command=on_clear_click)
    clear_btn.grid(row=3, column=3) 

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
        entry.delete(0, END)
      
    return handle
