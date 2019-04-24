from tkinter import *

class TextOutput:
  def __init__(self, root):
    root.columnconfigure(0, minsize=root.winfo_width() - 15)

    Label(root, text="Output:").grid(row=0, sticky="W")

    scrollbar = Scrollbar(root)
    self.text_cont = Text(root, height=15)

    self.text_cont.grid(row=1, column=0, sticky="WENS")
    scrollbar.grid(row=1, column=1, sticky="NS")
  
    self.text_cont.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=self.text_cont.yview)
  
  def println(self, text):
    self.text_cont.insert(END, text + '\n')