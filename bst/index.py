import uuid
from bst.node import Node
from bst.utils import * 

class BST:
  root = None
  size = 0 

  def __init__(self, root = None):
    self.root = root
    self.size = get_size(root)

  def add(self, key):
    node = Node(uuid.uuid4(), key)

    if not self.root:
      self.root = node 
      self.size += 1
    else:
      inserted = insert(self.root, node)
      if inserted:
        self.size += 1

  def remove(self, key):
    node_to_remove = find(self.root, key)
    if not node_to_remove:
      return

    self.size -= 1

    # remove root
    if node_to_remove.id == self.root.id:
      left_max = find_max(self.root.left)
      left_max.substitute_with_child('left')
      left_max.right = self.root.right
      left_max.left = self.root.left

      self.root = left_max
      return

    # remove node with only left child or no childs
    if not node_to_remove.right:
      node_to_remove.substitute_with_child('left')
      return
    
    # remove node with only right child or no childs
    if not node_to_remove.left:
      node_to_remove.substitute_with_child('right')
      return

    # remove node with both childs 
    left_max = find_max(node_to_remove.left)
    left_max.substitute_with_child('left')
    left_max.right = node_to_remove.right
    left_max.left = node_to_remove.left
    node_to_remove.substitute_with(left_max)

  def find(self, key):
    res = find(self.root, key)
    if res:
      return res.id
  
  def max(self):
    return find_max(self.root)
  
  def min(self):
    return find_min(self.root)
  
  def subtree(self, key):
    return BST(find(self.root, key))

  def draw(self, canvas):
    draw(self.root, canvas, { 'x': 400, 'y': 10}, None, 1, self.size)