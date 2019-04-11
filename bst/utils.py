def insert(root, node):
  if node.key > root.key:
    if root.right == None:
      root.right = node
    else:
      insert(root.right, node)

  elif node.key < root.key:
    if root.left == None:
      root.left = node
    else:
      insert(root.left, node)
    