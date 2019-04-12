def insert(root, node):
  if node.key > root.key:
    if root.right == None:
      node.parent = root
      root.right = node
    else:
      insert(root.right, node)

  elif node.key < root.key:
    if root.left == None:
      node.parent = root
      root.left = node
    else:
      insert(root.left, node)

def find(root, key):
  if not root:
    return None

  if key > root.key:
    return find(root.right, key)

  if key < root.key:
    return find(root.left, key)
  
  return root

def find_max(root):
  if not root.right:
    return root

  return find_max(root.right)

def find_min(root):
  if not root.left:
    return root
  
  return find_min(root.left)

def get_size(root):
  if not root:
    return 0

  if not root.left and not root.right:
    return 1
  
  return get_size(root.left) + get_size(root.right)
