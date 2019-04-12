import uuid
from bst.node import Node
from bst.utils import insert, find, find_max

class BST:
  root = None
  size = 0 

  def add(self, key):
    node = Node(uuid.uuid4(), key)
    if not self.root:
      self.root = node 
    else:
      insert(self.root, node)

    self.size += 1
  
  def remove(self, key):
    node_to_remove = find(self.root, key)
    if not node_to_remove:
      return

    self.size -= 1

    if node_to_remove.id == self.root.id:
      left_max = find_max(self.root.left)
      left_max.substitute_with_child('left')
      left_max.right = self.root.right
      left_max.left = self.root.left

      self.root = left_max
      return

    if not node_to_remove.right:
      node_to_remove.substitute_with_child('left')
      return
    
    if not node_to_remove.left:
      node_to_remove.substitute_with_child('right')
      return
    
    left_max = find_max(node_to_remove.left)
    left_max.substitute_with_child('left')
    left_max.right = node_to_remove.right
    left_max.left = node_to_remove.left
    node_to_remove.substitute_with(left_max)

  def find(self, key):
    res = find(self.root, key)
    if res:
      return res.id