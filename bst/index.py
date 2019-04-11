from bst.node import Node
from bst.utils import insert

class BST:
  root = None
  size = 0

  def add(self, key):
    if self.root == None:
      self.root = Node(self.size, key)
    else:
      insert(self.root, Node(self.size, key))