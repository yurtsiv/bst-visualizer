def insert(root, node):
  if root.key == node.key:
    return False

  if node.key > root.key:
    if root.right == None:
      node.parent = root
      root.right = node
      return True
    
    insert(root.right, node)

  elif node.key < root.key:
    if root.left == None:
      node.parent = root
      root.left = node
      return True

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

def draw(root, canvas, parent_pos, side, level, size):
  position = { 'y': parent_pos['y'] + 20, 'x': None }
  if not side:
    position = parent_pos
  elif side == 'left':
    position['x'] = parent_pos['x'] - (size * 10) / level 
  else:
    position['x'] = parent_pos['x'] + (size * 10) / level
  
  canvas.create_text(position['x'], position['y'], text=root.key)
  canvas.create_line(parent_pos['x'], parent_pos['y'], position['x'], position['y'])

  if not root.left and not root.right:
    return

  if root.left:
    draw(root.left, canvas, position, 'left', level+1, size)
  
  if root.right:
    draw(root.right, canvas, position, 'right', level+1, size)