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
  else:
    return find_max(root.right)