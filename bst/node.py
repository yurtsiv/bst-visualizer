class Node:
  id, key, left, right = None, None, None, None

  def __init__(self, id, key):
    self.id = id
    self.key = key
  
  def set_right(self, node):
    self.right = node
  
  def set_left(self, node):
    self.left = node

